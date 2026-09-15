import argparse
import json
import os
import time
from io import BytesIO
from typing import Optional

import polars as pl
import requests
from github import Github

from cfa.dataops import datacat
from cfa.dataops.soda import Query

dataset = datacat.public.stf.nssp_ed
dataset_id = dataset.config["source"]["id"]
access_token = os.getenv("CDC_SODA_API_TOKEN")

MAX_PAGE_RETRIES = 5
RETRY_BACKOFF_SECONDS = 5


def filter_api_cols(data: pl.DataFrame) -> pl.DataFrame:
    """
    Filter the DataFrame to only include columns that are present in the API response.

    Args:
        data (pl.DataFrame): The DataFrame to filter.

    Returns:
        pl.DataFrame: The filtered DataFrame containing only the API columns.
    """
    api_cols = [
        "week_end",
        "geography",
        "county",
        "ed_trends_covid",
        "ed_trends_influenza",
        "ed_trends_rsv",
        "hsa",
        "hsa_counties",
        "hsa_nci_id",
        "fips",
        "trend_source",
        "buildnumber",
        "percent_visits_combined",
        "percent_visits_covid",
        "percent_visits_influenza",
        "percent_visits_rsv",
        "percent_visits_smoothed",
        "percent_visits_smoothed_covid",
        "percent_visits_smoothed_1",
        "percent_visits_smoothed_rsv",
    ]

    result = data.with_columns(
        [
            pl.lit(None).alias(col)
            for col in api_cols
            if col not in data.columns
        ]
    ).select(api_cols)

    return result


def etl_archive():
    """
    For fetching the archived versions of the NSSP ED data from the GitHub repo. This will not need to be run after
    etl workflow below is automated for CFA.
    """
    g = Github()

    repo_name = dataset.config["source"]["archive"]["repo"]
    file_path = dataset.config["source"]["archive"]["path"]
    current_extracted_versions = set(dataset.extract.get_versions())

    repo = g.get_repo(repo_name)
    commits = repo.get_commits(path=file_path)

    # GitHub returns commits newest first. Keep the newest snapshot for each
    # date because versions are stored by date, not commit SHA.
    commits_by_date = {}
    for c in commits:
        date = c.commit.author.date.strftime("%Y-%m-%d")
        commits_by_date.setdefault(date, c.sha)

    # get ordered dates that are not already extracted. If none, exit early.
    new_dates = sorted(
        date
        for date in commits_by_date
        if date not in current_extracted_versions
    )
    if not new_dates:
        print("No new versions found in archive.")
        return

    # Download and load each new version. The extract version is the resume marker, so write it only after load succeeds.
    for nd in new_dates:
        sha = commits_by_date[nd]
        file = repo.get_contents(file_path, ref=sha)
        raw_url = file.download_url
        if not raw_url:
            raise RuntimeError(
                f"No download URL found for {file_path} at {sha}"
            )

        print(f"Downloading and loading {nd} sha {sha} from archive...")
        response = requests.get(raw_url, timeout=60)
        response.raise_for_status()
        data = response.content

        # Validate and transform before writing either output. The extract
        # version is the resume marker, so write it only after load succeeds.
        # format columns matching data.cdc.gov API
        data_api = filter_api_cols(data=pl.read_parquet(BytesIO(data)))
        df_t = transform(data_api)
        buffer = BytesIO()
        try:
            df_t.write_parquet(buffer)
            dataset.load.write_blob(
                file_buffer=buffer.getvalue(),
                path_after_prefix=f"{nd}/data.parquet",
                auto_version=False,
            )
        finally:
            buffer.close()

        dataset.extract.write_blob(
            file_buffer=data,
            path_after_prefix=f"{nd}/data.parquet",
            auto_version=False,
        )
        print("File downloaded successfully.")


def get_updated_date() -> str:
    response = requests.get(
        f"https://data.cdc.gov/api/views/metadata/v1/{dataset_id}", timeout=10
    )
    response.raise_for_status()
    r = response.json()
    updated_at = r.get("dataUpdatedAt")
    if not updated_at:
        raise ValueError(
            "CDC metadata response did not include 'dataUpdatedAt'"
        )
    return updated_at.split("T")[0]


def check_for_new_data() -> bool:
    versions = dataset.extract.get_versions()
    return not versions or versions[0] < get_updated_date()


def extract(
    app_token: Optional[str] = access_token,
) -> pl.DataFrame:
    """For extracting raw data from data.cdc.gov

    Args:
        app_token (Optional[str]): Application token for accessing the CDC API

    Returns:
        pl.DataFrame: Polars DataFrame containing the requested data
    """

    dfs = []
    parts = []
    for attempt in range(MAX_PAGE_RETRIES):
        try:
            # Recreate the iterator for each attempt so a failure after some
            # pages have been returned restarts the complete query.
            q = Query(
                domain=dataset.config["source"]["domain"],
                id=dataset.config["source"]["id"],
                app_token=app_token,
            )
            dfs = []
            parts = []
            for i in q.get_pages():
                dfs.append(pl.from_dicts(i, infer_schema_length=None))
                parts.append(bytes(json.dumps(i, indent=2), "utf-8"))
            break
        except (requests.exceptions.RequestException, TimeoutError) as exc:
            if attempt == MAX_PAGE_RETRIES - 1:
                raise
            delay = RETRY_BACKOFF_SECONDS * (2**attempt)
            print(
                f"SODA page request failed ({exc}); retrying in {delay} "
                f"seconds for attempt ({attempt + 1}/{MAX_PAGE_RETRIES})..."
            )
            time.sleep(delay)
    updated_date = get_updated_date()
    dataset.extract.write_blob(
        file_buffer=parts,
        path_after_prefix=f"{updated_date}/part.json",
        auto_version=False,
    )

    data = pl.concat(dfs, how="diagonal")

    return data


def transform(data: pl.DataFrame) -> pl.DataFrame:
    """
    Transform the raw data into the desired format.

    Args:
        data (pl.DataFrame): Raw data as extracted by `extract`

    Returns:
        pl.DataFrame: Transformed data
    """
    # Convert week_end to datetime[ms]
    try:
        data_t = data.with_columns(
            pl.col("week_end").str.to_date(format="%Y-%m-%dT%H:%M:%S.000")
        )
    except Exception as e:
        try:
            # try alternative format
            data_t = data.with_columns(
                pl.col("week_end").str.to_date(format="%Y-%m-%d")
            )
        except Exception as ex:
            print(
                f"week_end left unchanged. Error converting week_end to datetime: {e}; {ex}"
            )
            data_t = data
    # convert buildnumber to date
    try:
        data_t = data_t.with_columns(
            pl.col("buildnumber").str.to_date(format="%Y-%m-%d")
        )
    except Exception as e:
        try:
            # try alternative column name
            data_t = data_t.with_columns(
                pl.col("BuildNumber").str.to_date(format="%Y-%m-%d")
            )
            # rename column to buildnumber
            data_t = data_t.rename({"BuildNumber": "buildnumber"})
        except Exception as ex:
            print(
                f"buildnumber left unchanged. Error converting buildnumber to datetime: {e}; {ex}"
            )

    try:
        # Convert all columns starting with percent to float
        cols = [col for col in data_t.columns if col.startswith("percent")]
        data_t = data_t.with_columns(
            pl.col(cols).cast(pl.Float64, strict=False)
        )
    except Exception as e:
        print(f"Error converting columns to Float64: {e}")

    return data_t


def load(data: pl.DataFrame) -> None:
    """
    Load the transformed data to the desired destination.

    Args:
        data (pl.DataFrame): Transformed data as produced by `transform`
    """
    buffer = BytesIO()
    data.write_parquet(buffer)
    updated_date = get_updated_date()
    dataset.load.write_blob(
        file_buffer=buffer.getvalue(),
        path_after_prefix=f"{updated_date}/data.parquet",
        auto_version=False,
    )
    buffer.close()


def etl_if_new(app_token: Optional[str] = access_token) -> None:
    """Run the ETL process only if there is new data available.

    Args:
        app_token (Optional[str]): Application token for accessing the CDC API
    """
    if check_for_new_data():
        print("New data available. Running ETL process.")
        raw = extract(app_token)
        transformed = transform(raw)
        load(transformed)
    else:
        print("No new data available. Skipping ETL process.")


def etl() -> None:
    """
    Execute the ETL process: extract, transform, and load.
    """
    parser = argparse.ArgumentParser(
        description="ETL process for NSSP ED data"
    )
    parser.add_argument(
        "--app-token",
        type=str,
        default=access_token,
        help="CDC SODA API application token",
    )
    parser.add_argument(
        "--skip-extract",
        action="store_true",
        help="only run transform and load steps on latest extracted data",
    )
    parser.add_argument(
        "--use_version",
        type=str,
        default="latest",
        help="if skipping extract, which version to use, default is 'latest'",
    )
    args = parser.parse_args()
    if args.skip_extract:
        raw_data = dataset.extract.get_dataframe(
            output="pl", version=args.use_version
        )
    else:
        raw_data = extract(app_token=args.app_token)
    transformed_data = transform(raw_data)
    load(transformed_data)
