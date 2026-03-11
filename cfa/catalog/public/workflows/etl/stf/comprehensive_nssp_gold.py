from datetime import datetime
from types import SimpleNamespace

import polars as pl
import duckdb

from utils.comp_nssp_azure_utils import AZURE_CONSTANTS, get_latest_archival_path, upload_latest_df_to_azure
from utils.comp_nssp_duckdb_utils import setup_duckdb

from cfa.cloudops.blob_helpers import read_blob_stream
from cfa.dataops import datacat

dataset = datacat.public.stf.comprehensive_nssp_gold
source_blob = SimpleNamespace(**dataset.config["source"]["storage_location"])


def create_latest_comprehensive() -> pl.DataFrame:
    #try setting up duckdb
    try:
        setup_duckdb()
    except Exception as e1:
        raise RuntimeError(f"Failed to set up DuckDB connection: {e1}")
    
    #try updating latest_comprehensive dataset
    try:
        comprehensive_df = update_latest_comprehensive()
        if comprehensive_df.is_empty():
            raise ValueError("The resulting comprehensive DataFrame is empty.")
        upload_latest_df_to_azure(comprehensive_df)
        return comprehensive_df
    except Exception as e2:
        raise RuntimeError(f"Error processing latest comprehensive NSSP ED visit data: {e2}")
    

def generate_full_dataset() -> None:
    return None

def copy_file(df: pl.DataFrame) -> None:
    date = datetime.now().isoformat().split("T")[0]
    dataset.load.save_dataframe(
        df,
        path_after_prefix=f"{date}/data.parquet",
    )

def update_latest_comprehensive() -> None:
    #create the latest comprehensive dataset
    latest_comprehensive_df = create_latest_comprehensive()
    #upload the latest comprehensive dataset to Azure Blob Storage
    upload_latest_df_to_azure(latest_comprehensive_df)
    #copy the dataset to the versioned path in the data catalog
    copy_file(latest_comprehensive_df)