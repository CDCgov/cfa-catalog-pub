from types import SimpleNamespace

import polars as pl
import tqdm

from cfa.cloudops.blob_helpers import read_blob_stream, walk_blobs_in_container
from cfa.dataops import datacat

dataset = datacat.public.stf.nssp_gold
source_blob = SimpleNamespace(**dataset.config["source"]["storage_location"])


def copy_missing_files() -> None:
    nssp_files = sorted(
        [
            i["name"].removeprefix(source_blob.prefix).removesuffix("/")
            for i in walk_blobs_in_container(
                account_name=source_blob.account,
                container_name=source_blob.container,
                name_starts_with=source_blob.prefix,
            )
        ],
        reverse=True,
    )
    cached_versions = dataset.load.get_versions()

    files_to_copy = [
        i
        for i in nssp_files
        if i.endswith(".parquet")
        and i.removesuffix(".parquet") not in cached_versions
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
                blob_url=f'{source_blob.prefix.removesuffix("/")}/{file}',
            ).content_as_bytes()
        )

        # if there is some transformation to the original data that should be performed before saving
        # make those transformations to the dataframe here

        dataset.load.save_dataframe(
            df,
            path_after_prefix=f"{file.removesuffix('.parquet')}/data.parquet",
        )
