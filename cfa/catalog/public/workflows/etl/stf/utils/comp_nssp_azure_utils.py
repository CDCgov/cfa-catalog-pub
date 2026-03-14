import logging
from io import BytesIO
from types import SimpleNamespace

import polars as pl
from azure.identity import EnvironmentCredential
from azure.storage.blob import BlobServiceClient

from cfa.dataops import datacat

logger = logging.getLogger(__name__)

dataset = datacat.public.stf.comprehensive_nssp_gold
source_blob = SimpleNamespace(**dataset.config["source"]["storage_location"])

account = source_blob.account
container = source_blob.container

AZURE_CONSTANTS = {
    "storage_account_url": f"https://{account}.blob.core.windows.net/",
    "output_filename": "stf_latest_comprehensive.parquet",
    "all_gold_path": f"az://{container}/gold/",
    "gold_archival_container": "nssp-archival-vintages",
    "latest_comprehensive_path": f"az://{container}/latest_comprehensive.parquet",
    "nssp_etl_container": "nssp-etl",
}


def obtain_sp_credential() -> EnvironmentCredential:
    """Obtains service principal credentials from Azure.
    Returns:
        Instance of EnvironmentCredential.
    Raises:
        LookupError if credential not found.
    """

    # The EnvironmentCredential reads from the environment directly
    # if running locally. Check that SP credentials
    # are in environment if running locally.
    sp_credential = EnvironmentCredential()

    return sp_credential


def instantiate_blob_service_client(
    sp_credential: EnvironmentCredential | None = None, account_url: str = ""
) -> BlobServiceClient:
    """Function to instantiate blob service client to interact
    with Azure Storage.
    Args:
        sp_credential (EnvironmentCredential): Service principal credential object
        for use in authenticating with Storage API.
        account_url (str): URL of the storage account.
    Returns:
        BlobServiceClient: Azure Blob Storage client
    Raises:
        ValueError: If sp_credential is invalid or BlobServiceClient
        fails to instantiate.
    """

    if not sp_credential:
        raise ValueError("Service principal credential not provided.")

    blob_service_client = BlobServiceClient(
        account_url, credential=sp_credential
    )

    return blob_service_client


def get_latest_archival_path() -> dict[str, str]:
    """Get the latest archival path for comprehensive data.
    Returns:
        str: Path to the latest archival gold data.
    """
    gold_archival_container = AZURE_CONSTANTS["gold_archival_container"]
    sp_credential = obtain_sp_credential()
    storage_client = instantiate_blob_service_client(
        sp_credential=sp_credential,
        account_url=AZURE_CONSTANTS["storage_account_url"],
    )
    container_client = storage_client.get_container_client(
        container=gold_archival_container
    )
    all_archival_paths = []
    for blob in container_client.list_blobs(name_starts_with="gold/"):
        if blob.name.endswith(".parquet"):
            all_archival_paths.append(blob.name.replace("gold/", ""))

    latest_vintage = max(all_archival_paths)
    latest_vintage_date = latest_vintage.replace(".parquet", "")
    latest_vintage_full_path = (
        f"az://{gold_archival_container}/gold/{latest_vintage}"
    )
    return {
        "latest_vintage_date": latest_vintage_date,
        "latest_vintage_full_path": latest_vintage_full_path,
    }


def get_latest_gold_dates(ref_date: str) -> list[str]:
    """Get the latest gold dates after a given report date.
    Args:
        ref_date (str): Report date in ISO format.
    Returns:
        list[str]: List of paths to the latest gold files.
    """
    sp_credential = obtain_sp_credential()
    storage_client = instantiate_blob_service_client(
        sp_credential=sp_credential,
        account_url=AZURE_CONSTANTS["storage_account_url"],
    )
    container_client = storage_client.get_container_client(
        container="nssp-etl"
    )
    latest_gold_dates = []
    for blob in container_client.list_blobs(name_starts_with="gold/"):
        clean_name = blob.name.replace("gold/", "").replace(".parquet", "")
        if clean_name >= ref_date:
            latest_gold_dates.append(clean_name)

    return latest_gold_dates


def upload_latest_df_to_azure(
    df: pl.DataFrame, alternate_output_filename: str = ""
) -> None:
    """
    Uploads a DataFrame to Azure Blob Storage in parquet format.
    Args:
        df (DataFrame): DataFrame to upload.
        alternate_output_filename (str): Optional alternate filename for the uploaded parquet file.
    """

    # DuckDB does not support writing to Azure Blob Storage directly.
    # So we write the dataframe to parquet in a buffer of bytes, and
    # write the bytes to Azure Blob Storage.
    # See: https://stackoverflow.com/a/68717897

    try:
        sp_credential = obtain_sp_credential()
        storage_client = instantiate_blob_service_client(
            sp_credential=sp_credential,
            account_url=AZURE_CONSTANTS["storage_account_url"],
        )
        container_client = storage_client.get_container_client(
            container=AZURE_CONSTANTS["nssp_etl_container"]
        )
        parquet_stream = BytesIO()
        df.write_parquet(parquet_stream)
        # change the stream position back to the beginning after writing
        parquet_stream.seek(0)
        blob_name = AZURE_CONSTANTS["output_filename"]
        if alternate_output_filename != "":
            # If an alternate output filename is provided, use it instead
            # of the default output filename.
            # This is useful for testing purposes.
            blob_name = alternate_output_filename
        container_client.upload_blob(
            name=blob_name, data=parquet_stream, overwrite=True
        )
    except Exception as e:
        logger.error(f"Error uploading DataFrame to Azure Blob Storage: {e}")
        raise e
