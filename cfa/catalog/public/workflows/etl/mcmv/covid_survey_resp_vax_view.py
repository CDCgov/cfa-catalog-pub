import os
from io import BytesIO
from typing import Optional

import nisapi
import polars as pl
import requests
from nisapi.clean import clean_dataset

from cfa.dataops import datacat

dataset = datacat.public.mcmv.covid_survey_resp_vax_view

access_token = os.getenv("NIS_APP_TOKEN", None)

dataset_id = dataset.config["source"]["id"]

clean_args = nisapi._get_dataset_metadata(dataset_id, "cleaning_arguments")


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

    raw = nisapi._download_dataset(
        id=dataset_id,
        app_token=app_token,
    )

    buffer = BytesIO()
    raw.write_parquet(buffer)
    updated_date = get_updated_date()
    dataset.extract.write_blob(
        file_buffer=buffer.getvalue(),
        path_after_prefix=f"{updated_date}/data.parquet",
        auto_version=False,
    )
    buffer.close()

    return raw


def transform(raw_df: pl.DataFrame) -> pl.DataFrame:
    return clean_dataset(raw_df.lazy(), dataset_id, clean_args, "warn")


def load(data: pl.DataFrame) -> str:
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
    return f"{updated_date}/data.parquet"


def etl(app_token: Optional[str] = access_token) -> str:
    """Run the full ETL process: extract, transform, and load.

    Args:
        app_token (Optional[str]): Application token for accessing the CDC API
    """
    raw_df = extract(app_token)
    transformed_df = transform(raw_df)
    outpath = load(transformed_df)
    return outpath


def etl_if_new(app_token: Optional[str] = access_token) -> str:
    """Run the ETL process only if there is new data available.

    Args:
        app_token (Optional[str]): Application token for accessing the CDC API
    """
    v = dataset.extract.get_versions()
    newest = "0000-00-00"
    if v:
        newest = v[0].split("T")[0]
    updated_date = get_updated_date()
    if newest < updated_date:
        print("New data available. Running ETL process.")
        outpath = etl(app_token)
        print(f"ETL process completed. Data saved to {outpath}.")
    else:
        outpath = ""
        print("No new data available. ETL process will not run.")
    return outpath
