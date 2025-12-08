import argparse
import json
import os
from io import BytesIO
from typing import Optional

import polars as pl

from cfa.dataops import datacat
from cfa.dataops.soda import Query

dataset = datacat.public.stf.nhsn_hrd

access_token = os.getenv("CDC_SODA_API_TOKEN")


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

    dataset.extract.write_blob(
        file_buffer=parts, path_after_prefix="part.json", auto_version=True
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

    # Convert date columns to proper date types
    schema = {k: pl.Float64 for k, v in data.schema.items()}

    schema.update(
        {
            "weekendingdate": pl.Datetime(time_unit="ms"),
            "jurisdiction": pl.String,
        }
    )

    data_transformed = data.with_columns(
        pl.col(c).cast(dtype) for c, dtype in schema.items()
    )
    data_transformed = data_transformed.with_columns(
        pl.col("weekendingdate").dt.date()
    )

    # Additional transformations can be added here as needed examples:
    # - Renaming columns
    # - Filtering rows
    # - Creating new calculated columns

    return data_transformed


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
