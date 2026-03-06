from datetime import datetime
from types import SimpleNamespace

import polars as pl

from cfa.cloudops.blob_helpers import read_blob_stream
from cfa.dataops import datacat

dataset = datacat.public.stf.nssp_latest_comprehensive
source_blob = SimpleNamespace(**dataset.config["source"]["storage_location"])

file_to_copy = "latest_comprehensive.parquet"


def copy_file() -> None:
    df = pl.read_parquet(
        read_blob_stream(
            account_name=source_blob.account,
            container_name=source_blob.container,
            blob_url=file_to_copy,
        ).content_as_bytes()
    )

    date = datetime.now().isoformat().split("T")[0]
    dataset.load.save_dataframe(
        df,
        path_after_prefix=f"{date}/data.parquet",
    )
