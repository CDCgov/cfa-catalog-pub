import re
from types import SimpleNamespace

import polars as pl
import tqdm

from cfa.cloudops.blob_helpers import read_blob_stream, walk_blobs_in_container
from cfa.dataops import datacat

dataset = datacat.public.stf.nwss
source_blob = SimpleNamespace(**dataset.config["source"]["storage_location"])


def copy_missing_files() -> None:
    nwss_files = sorted(
        [
            i["name"].removesuffix("/")
            for i in walk_blobs_in_container(
                account_name=source_blob.account,
                container_name=source_blob.container,
            )
        ],
        reverse=True,
    )
    cached_versions = dataset.load.get_versions()

    date_pattern = re.compile(r"(\d{4}-\d{2}-\d{2})")

    files_to_copy = [
        i
        for i in nwss_files
        if i.startswith("NWSS-ETL-covid")
        and re.search(date_pattern, i).group(1) not in cached_versions
    ]

    if not files_to_copy:
        print("No new files to copy")
        return

    pbar = tqdm.tqdm(files_to_copy)
    for file in pbar:
        pbar.set_description(f"Copying {file}")
        df = pl.read_parquet(
            read_blob_stream(
                account_name=source_blob.account,
                container_name=source_blob.container,
                blob_url=f"{file}/bronze.parquet",
            ).content_as_bytes()
        )

        # if there is some transformation to the original data that should be performed before saving
        # make those transformations to the dataframe here
        date = re.search(date_pattern, file).group(1)

        dataset.load.save_dataframe(
            df,
            path_after_prefix=f"{date}/data.parquet",
        )
