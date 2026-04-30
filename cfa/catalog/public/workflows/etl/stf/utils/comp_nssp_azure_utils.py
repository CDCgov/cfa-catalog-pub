import logging
from types import SimpleNamespace

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
    "gold_archival_container": "nssp-archival-vintages",
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
