import os

import duckdb

from cfa.cloudops import CloudClient


def get_auth() -> dict:
    """Get authentication information."""
    cc = CloudClient(keyvault="cfa-predict")
    tenant_id = cc.cred.azure_tenant_id
    client_id = cc.cred.azure_client_id
    client_secret = cc.get_kv_secret(
        secret_name=cc.cred.azure_keyvault_sp_secret_id, keyvault="cfa-predict"
    )
    storage_account_name = cc.cred.azure_blob_storage_account
    if None in [tenant_id, client_id, client_secret, storage_account_name]:
        raise ValueError(
            "Missing required environment variables for Azure Blob Storage connection."
        )
    # save to env variables for SP login
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
