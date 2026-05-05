import os
import tempfile
from io import BytesIO
from typing import Optional

import nisapi
import polars as pl
from nisapi.clean import clean_dataset

from cfa.dataops import datacat

dataset = datacat.public.mcmv.parental_vax_intent_weekly

access_token = os.getenv("NIS_APP_TOKEN", None)

dataset_id = dataset.config["source"]["id"]

td = tempfile.TemporaryDirectory()

clean_args = nisapi._get_dataset_metadata(dataset_id, "cleaning_arguments")


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
    dataset.extract.write_blob(
        file_buffer=buffer.getvalue(),
        path_after_prefix="data.parquet",
        auto_version=True,
    )
    buffer.close()

    return raw


def transform(raw_df: pl.DataFrame) -> pl.DataFrame:
    return clean_dataset(raw_df.lazy(), dataset_id, clean_args, "warn")


def load(data: pl.DataFrame) -> None:
    """
    Load the transformed data to the desired destination.

    Args:
        data (pl.DataFrame): Transformed data as produced by `transform`
    """
    buffer = BytesIO()
    data.write_parquet(buffer)
    dataset.load.write_blob(
        file_buffer=buffer.getvalue(),
        path_after_prefix="data.parquet",
        auto_version=True,
    )
    buffer.close()


def etl(app_token: Optional[str] = access_token) -> None:
    """Run the full ETL process: extract, transform, and load.

    Args:
        app_token (Optional[str]): Application token for accessing the CDC API
    """
    raw_df = extract(app_token)
    transformed_df = transform(raw_df)
    load(transformed_df)
