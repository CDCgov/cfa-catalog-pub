import os

import duckdb
import polars as pl

from cfa.cloudops import CloudClient
from comp_nssp_azure_utils import AZURE_CONSTANTS, get_latest_gold_dates


def get_auth() -> dict:
    """Get authentication information."""
    cc = CloudClient(keyvault = "cfa-predict")
    tenant_id = cc.cred.azure_tenant_id
    client_id = cc.cred.azure_client_id
    client_secret = cc.get_kv_secret(secret_name  = cc.cred.azure_keyvault_sp_secret_id, keyvault = "cfa-predict")
    storage_account_name = cc.cred.azure_blob_storage_account
    if None in [tenant_id, client_id, client_secret, storage_account_name]:
        raise ValueError(
            "Missing required environment variables for Azure Blob Storage connection."
        )
    #save to env variables for SP login
    os.environ["AZURE_TENANT_ID"] = tenant_id
    os.environ["AZURE_CLIENT_ID"] = client_id
    os.environ["AZURE_CLIENT_SECRET"] = client_secret

    return {
        "tenant_id": tenant_id,
        "client_id": client_id,
        "client_secret": client_secret,
        "storage_account_name": storage_account_name,
    }


def setup_duckdb() -> None:
    """Set up connection to Azure Blob Storage."""
    auth_info = get_auth()

    # Needed for Linux runtimes to set up HTTP connection
    duckdb.sql("SET azure_transport_option_type='curl';")

    duckdb.sql(
        f"CREATE SECRET IF NOT EXISTS azure_spn \
                ( \
                    TYPE AZURE, \
                    PROVIDER SERVICE_PRINCIPAL, \
                    TENANT_ID '{auth_info['tenant_id']}', \
                    CLIENT_ID '{auth_info['client_id']}', \
                    CLIENT_SECRET '{auth_info['client_secret']}', \
                    ACCOUNT_NAME '{auth_info['storage_account_name']}' \
        );"
    )

def update_latest_comprehensive() -> pl.DataFrame:
    """Update latest comprehensive NSSP ED visit data."""
    all_gold_modern_path = AZURE_CONSTANTS["all_gold_path"]
    latest_comprehensive_path = AZURE_CONSTANTS["latest_comprehensive_path"]
    latest_report = duckdb.sql(
        f"SELECT MAX(report_date) FROM '{latest_comprehensive_path}';"
    ).fetchone()[0]
    latest_gold_dates = get_latest_gold_dates(latest_report.isoformat())

    if len(latest_gold_dates) > 1:
        current_comprehensive = duckdb.sql(
            f"SELECT * FROM '{latest_comprehensive_path}';"
        ).pl()

        # First, pull all data strictly before the max report date from the latest comprehensive
        historical_data = current_comprehensive.filter(
            pl.col("report_date") < latest_report
        )

        # Generate latest_comprehensive for each latest_gold_date and append to historical data
        # Only the latest report date should include all reference dates, this will collapse
        # the current highest report_date into one row per reference_date

        full_path = [
            f"{all_gold_modern_path}{date}.parquet" for date in latest_gold_dates
        ]
        comprehensive_for_dates = duckdb.sql(
            f"""
            WITH latest_report_dates AS
            (SELECT reference_date,
                    MAX(report_date) AS latest_report_date
            FROM read_parquet({full_path})
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
            FROM read_parquet({full_path}) AS ag
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
            FROM modern_vintages_mega;
            """
        ).pl()

        return pl.concat([comprehensive_for_dates, historical_data])
    return pl.DataFrame()