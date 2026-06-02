import re
from pathlib import Path
from types import SimpleNamespace

import polars as pl
import tqdm

from cfa.cloudops.blob_helpers import read_blob_stream, walk_blobs_in_container
from cfa.dataops import datacat

dataset = datacat.public.stf.param_estimates
source_blob = SimpleNamespace(**dataset.config["source"]["storage_location"])


def check_for_new_data() -> tuple[bool, list[str]]:
    param_files = sorted(
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
    pattern = re.compile(r"^(\d{4}-\d{2}-\d{2}).*\.parquet")

    files_to_copy = [
        f
        for f in param_files
        if (m := pattern.search(f)) and m.group(1) not in cached_versions
    ]
    return (len(files_to_copy) > 0, files_to_copy)


def copy_missing_files() -> Path:
    new_data, files_to_copy = check_for_new_data()

    if not new_data:
        print("No new files to copy")
        return

    pbar = tqdm.tqdm(files_to_copy)
    for file in pbar:
        pbar.set_description(f"Copying {file}")
        df = pl.read_parquet(
            read_blob_stream(
                account_name=source_blob.account,
                container_name=source_blob.container,
                blob_url=file,
            ).content_as_bytes()
        )

        # if there is some transformation to the original data that should be performed before saving
        # make those transformations to the dataframe here
        outpath = f"{file[0:10]}/data.parquet"
        dataset.load.save_dataframe(
            df,
            path_after_prefix=outpath,
        )
    return Path(outpath)
