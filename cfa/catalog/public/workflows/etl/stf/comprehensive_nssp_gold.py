from datetime import datetime
from types import SimpleNamespace

import polars as pl
from tqdm import tqdm

from cfa.dataops import datacat

from .utils.comp_nssp_version_utils import (
    clear_azure_credentials,
    get_all_gold_dates,
    get_gold_dates_before_ref,
    get_latest_comprehensive_for_date,
)

dataset = datacat.public.stf.comprehensive_nssp_gold
source_blob = SimpleNamespace(**dataset.config["source"]["storage_location"])


def copy_file(df: pl.DataFrame, date: str | None = None) -> None:
    if date is None:
        date = datetime.now().isoformat().split("T")[0]
    dataset.load.save_dataframe(
        df,
        path_after_prefix=f"{date}/data.parquet",
    )


# this function can backfill the comprehensive dataset based on all nssp gold dates
def generate_versioned_dataset() -> None:
    # get all available gold dates and existing versions in the data catalog
    versions = dataset.load.get_versions()
    gold_dates_sort = get_all_gold_dates()
    # get final list to run
    date_list = [date for date in gold_dates_sort if date not in versions]
    # get data for missing versions and upload
    for ref_date in tqdm(date_list):
        print(f"Generating comprehensive dataset for {ref_date}...")
        dates_available = get_gold_dates_before_ref(ref_date, gold_dates_sort)
        df = get_latest_comprehensive_for_date(dates_available)
        clear_azure_credentials()
        copy_file(df, ref_date)
    return None
