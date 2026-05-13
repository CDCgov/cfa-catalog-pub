import argparse
import json
import os
import re
from io import BytesIO, StringIO
from typing import Optional

import polars as pl
import requests
import yaml
from github import Github

from cfa.dataops import datacat
from cfa.dataops.soda import Query

dataset = datacat.public.stf.nhsn_hrd_prelim
dataset_id = dataset.config["source"]["id"]
access_token = os.getenv("CDC_SODA_API_TOKEN")


def etl_archive():
    """
    For fetching the archived versions of the NHSN HRD data from GitHub user repo. this will not need to be run after
    etl workflow below is automated for CFA.
    """
    g = Github()
    repo = g.get_repo(dataset.config["source"]["archive"]["repo"])
    contents = repo.get_contents(dataset.config["source"]["archive"]["path"])
    current_extracted_versions = dataset.extract.get_versions()
    # extract metadata file
    download_url = "https://raw.githubusercontent.com/paulocv/respiratory_archive/main/datasets/nhsn_weekly_jurisdiction/metadata.yaml"
    r = requests.get(download_url)
    metadata = yaml.safe_load(r.text)
    prelim_files = [
        file["filename"]
        for file in metadata["files"]
        if file["release"] == "prelim"
    ]
    for file in contents:
        version_match = re.search(
            r"nhsn_(\d{4}\-\d{2}\-\d{2})\.csv", file.name
        )
        if version_match:
            # check if file is prelim
            if file.name in prelim_files:
                version_date = version_match.group(1) + "T00-00-00"
                if version_date not in current_extracted_versions:
                    print(
                        f"Downloading and loading {file.name} from archive..."
                    )
                    # Extract file from GitHub if isn't already cached
                    r = requests.get(file.download_url)
                    data = r.text
                    dataset.extract.write_blob(
                        file_buffer=bytes(data, "utf-8"),
                        path_after_prefix=f"{version_date}/{file.name}",
                        auto_version=False,
                    )
                    # Transform the data
                    df_t = transform(pl.read_csv(StringIO(data)))
                    # Load the transformed data
                    buffer = BytesIO()
                    df_t.write_parquet(buffer)
                    dataset.load.write_blob(
                        file_buffer=buffer.getvalue(),
                        path_after_prefix=f"{version_date}/data.parquet",
                        auto_version=False,
                    )
                    buffer.close()


def get_updated_date() -> str:
    response = requests.get(
        f"https://data.cdc.gov/api/views/metadata/v1/{dataset_id}", timeout=10
    )
    r = response.json()
    return r["dataUpdatedAt"].split("T")[0] + "T00-00-00"


def extract(
    app_token: Optional[str] = access_token,
) -> pl.DataFrame:
    """For extracting raw data from data.cdc.gov

    Args:
        app_token (Optional[str]): Application token for accessing the CDC API

    Returns:
        pl.DataFrame: Polars DataFrame containing the requested data, plus a
            `date` column that is the Sunday that starts each week
    """

    q = Query(
        domain=dataset.config["source"]["domain"],
        id=dataset.config["source"]["id"],
        app_token=app_token,
    )
    dfs = []
    parts = []
    for i in q.get_pages():
        dfs.append(pl.from_dicts(i))
        parts.append(bytes(json.dumps(i, indent=2), "utf-8"))
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

    # Convert weekendingdate to datetime[ms]
    try:
        data_t = data.with_columns(
            pl.col("weekendingdate").str.to_date(
                format="%Y-%m-%dT%H:%M:%S.000"
            )
        )
    except Exception as e:
        try:
            # try alternative format
            data_t = data.with_columns(
                pl.col("weekendingdate").str.to_date(format="%Y-%m-%d")
            )
        except Exception as ex:
            print(
                f"weekendingdate left unchanged. Error converting weekendingdate to datetime: {e}; {ex}"
            )
            data_t = data

    # Ensure jurisdiction is string type
    try:
        data_t = data_t.with_columns(pl.col("jurisdiction").cast(pl.String))
    except Exception as e:
        print(f"Error converting jurisdiction to string: {e}")
        raise

    try:
        # Convert all columns except specific ones to float
        data_t = data_t.with_columns(
            pl.exclude(["weekendingdate", "jurisdiction"]).cast(
                pl.Float64, strict=False
            )
        )
    except Exception as e:
        print(f"Error converting columns to Float64: {e}")

    # Additional transformations can be added here as needed examples:
    # - Renaming columns
    # - Filtering rows
    # - Creating new calculated columns

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
    v = dataset.extract.get_versions()
    newest = v[0].split("T")[0]
    response = requests.get(
        f"https://data.cdc.gov/api/views/metadata/v1/{dataset_id}"
    )
    r = response.json()
    updated_date = r["dataUpdatedAt"].split("T")[0]
    if newest < updated_date:
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
        description="ETL process for NHSN HRD data"
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
