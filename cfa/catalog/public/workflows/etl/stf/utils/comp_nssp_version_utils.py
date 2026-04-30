import logging
import os

import duckdb

from .comp_nssp_azure_utils import (
    AZURE_CONSTANTS,
    get_latest_archival_path,
    instantiate_blob_service_client,
    obtain_sp_credential,
)
from .comp_nssp_duckdb_utils import setup_duckdb

logger = logging.getLogger(__name__)


# gets the file names to use in the query based on ref date and all dates less than or equal to ref date
def get_gold_dates_before_ref(
    ref_date: str, all_dates: list[str]
) -> list[str]:
    dates_available = [date for date in all_dates if date <= ref_date]
    files = [f"az://nssp-etl/gold/{date}.parquet" for date in dates_available]
    return files


# run the query to get the latest comprehensive dataset for the files passed in
def get_latest_comprehensive_for_date(files):
    setup_duckdb()
    latest_archival_path = get_latest_archival_path()[
        "latest_vintage_full_path"
    ]
    comprehensive_df = duckdb.sql(
        f"""
            WITH latest_report_dates AS
            (SELECT reference_date,
                    MAX(report_date) AS latest_report_date
            FROM read_parquet({files})
            GROUP BY reference_date),
                modern_vintages_mega AS
            (SELECT ag.report_date,
                    ag.reference_date,
                    ag.asof,
                    ag.metric,
                    ag.geo_type,
                    ag.geo_value,
                    ag.run_id,
                    ag.disease,
                    SUM(ag.value) AS value
            FROM read_parquet({files}) AS ag
            JOIN latest_report_dates AS lrd ON ag.reference_date = lrd.reference_date
            AND ag.report_date = lrd.latest_report_date
            GROUP BY ag.report_date,
                        ag.reference_date,
                        ag.asof,
                        ag.metric,
                        ag.geo_type,
                        ag.geo_value,
                        ag.run_id,
                        ag.disease)
            SELECT report_date,
                reference_date,
                metric,
                geo_type,
                geo_value,
                disease,
                value
            FROM modern_vintages_mega
            UNION ALL
            SELECT report_date,
                reference_date,
                metric,
                geo_type,
                geo_value,
                disease,
                value
            FROM '{latest_archival_path}'
            WHERE reference_date < (SELECT MIN(reference_date) FROM modern_vintages_mega);
        """
    ).pl()
    return comprehensive_df


# gets all available nssp gold dates
def get_all_gold_dates():
    setup_duckdb()
    etl_gold_container = AZURE_CONSTANTS["nssp_etl_container"]
    sp_credential = obtain_sp_credential()
    storage_client = instantiate_blob_service_client(
        sp_credential=sp_credential,
        account_url=AZURE_CONSTANTS["storage_account_url"],
    )
    container_client = storage_client.get_container_client(
        container=etl_gold_container
    )
    all_gold_paths = []
    for blob in container_client.list_blobs(name_starts_with="gold/"):
        all_gold_paths.append(blob.name.replace("gold/", ""))

    gold_dates = [
        file.replace("gold/", "").replace(".parquet", "")
        for file in all_gold_paths
        if file.endswith(".parquet")
    ]
    gold_dates_sort = sorted(gold_dates)
    return gold_dates_sort


# clears azure credentials from environment variables before uploading to avoid credential mismatches
def clear_azure_credentials():
    if "AZURE_TENANT_ID" in os.environ:
        del os.environ["AZURE_TENANT_ID"]
    if "AZURE_CLIENT_SECRET" in os.environ:
        del os.environ["AZURE_CLIENT_SECRET"]
    if "AZURE_CLIENT_ID" in os.environ:
        del os.environ["AZURE_CLIENT_ID"]
