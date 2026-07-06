from collections.abc import Sequence
from types import SimpleNamespace
from typing import Any, Literal, overload

import pandas as pd
import polars as pl

from .reporting.catalog import NotebookEndpoint

def get_all_catalogs() -> list[tuple[str, str, str]]: ...

class CatalogNamespace(SimpleNamespace):
    pass

class DatasetEndpoint:
    config_path: str
    defaults: dict[str, Any]
    config: dict[str, Any]
    __ns_str__: str
    _ledger_location: dict[str, Any]

class BlobEndpoint:
    account: str
    container: str
    prefix: str
    ledger_location: dict[str, Any]
    is_ledger: bool
    __ns_str__: str
    def write_blob(
        self,
        file_buffer: bytes | Sequence[bytes],
        path_after_prefix: str,
        auto_version: bool = False,
        append: bool = False,
    ) -> None: ...
    def read_blobs(
        self,
        version_spec: str | None = None,
        selection: Literal["newest", "oldest", "all"] = "newest",
        print_version: bool = True,
    ) -> list[bytes]: ...
    def read_csv(self, suffix: str) -> pd.DataFrame: ...
    def get_versions(self) -> list[str]: ...
    def get_file_ext(
        self,
        version_spec: str | None = None,
        selection: Literal["newest", "oldest", "all"] = "newest",
    ) -> str: ...
    def download_version_to_local(
        self,
        local_path: str,
        version_spec: str | None = None,
        force: bool = False,
        selection: Literal["newest", "oldest", "all"] = "newest",
    ) -> bool: ...
    @overload
    def get_dataframe(
        self,
        output: Literal["pandas", "pd"] = "pandas",
        version_spec: str | None = None,
        selection: Literal["newest", "oldest"] = "newest",
    ) -> pd.DataFrame: ...
    @overload
    def get_dataframe(
        self,
        output: Literal["polars", "pl"],
        version_spec: str | None = None,
        selection: Literal["newest", "oldest"] = "newest",
    ) -> pl.DataFrame: ...
    @overload
    def get_dataframe(
        self,
        output: Literal["pl_lazy", "lazy"],
        version_spec: str | None = None,
        selection: Literal["newest", "oldest"] = "newest",
    ) -> pl.LazyFrame: ...
    def ledger_entry(self, action: str) -> None: ...
    def save_dataframe(
        self,
        df: pd.DataFrame | pl.DataFrame,
        path_after_prefix: str,
        file_format: str = "parquet",
        auto_version: bool = False,
    ) -> None: ...
    def save_file_to_blob(
        self,
        file_path: str,
        path_after_prefix: str,
        auto_version: bool = False,
    ) -> None: ...
    def save_dir_to_blob(
        self,
        dir_path: str,
        path_after_prefix: str,
        auto_version: bool = False,
    ) -> None: ...

def dict_to_sn(
    d: Any,
    defaults: dict[str, Any] | None = None,
    ns: str = "",
) -> CatalogNamespace: ...

class _DataCatalogPublicReferenceCenpop2020Dataset(DatasetEndpoint):
    config: dict[str, Any]
    data: BlobEndpoint

class _DataCatalogPublicReferenceStateHhsRegionsDataset(DatasetEndpoint):
    config: dict[str, Any]
    data: BlobEndpoint

class _DataCatalogPublicReferenceNamespace(CatalogNamespace):
    cenpop2020: _DataCatalogPublicReferenceCenpop2020Dataset
    state_hhs_regions: _DataCatalogPublicReferenceStateHhsRegionsDataset

class _DataCatalogPublicStfComprehensiveNsspGoldDataset(DatasetEndpoint):
    config: dict[str, Any]
    load: BlobEndpoint

class _DataCatalogPublicStfNhsnHrdDataset(DatasetEndpoint):
    config: dict[str, Any]
    extract: BlobEndpoint
    load: BlobEndpoint

class _DataCatalogPublicStfNhsnHrdPrelimDataset(DatasetEndpoint):
    config: dict[str, Any]
    extract: BlobEndpoint
    load: BlobEndpoint

class _DataCatalogPublicStfNsspGoldV1Dataset(DatasetEndpoint):
    config: dict[str, Any]
    load: BlobEndpoint

class _DataCatalogPublicStfNsspGoldV2Dataset(DatasetEndpoint):
    config: dict[str, Any]
    load: BlobEndpoint

class _DataCatalogPublicStfNwssDataset(DatasetEndpoint):
    config: dict[str, Any]
    extract: BlobEndpoint
    load: BlobEndpoint

class _DataCatalogPublicStfParamEstimatesDataset(DatasetEndpoint):
    config: dict[str, Any]
    load: BlobEndpoint

class _DataCatalogPublicStfNamespace(CatalogNamespace):
    comprehensive_nssp_gold: _DataCatalogPublicStfComprehensiveNsspGoldDataset
    nhsn_hrd: _DataCatalogPublicStfNhsnHrdDataset
    nhsn_hrd_prelim: _DataCatalogPublicStfNhsnHrdPrelimDataset
    nssp_gold_v1: _DataCatalogPublicStfNsspGoldV1Dataset
    nssp_gold_v2: _DataCatalogPublicStfNsspGoldV2Dataset
    nwss: _DataCatalogPublicStfNwssDataset
    param_estimates: _DataCatalogPublicStfParamEstimatesDataset

class _DataCatalogPublicNamespace(CatalogNamespace):
    reference: _DataCatalogPublicReferenceNamespace
    stf: _DataCatalogPublicStfNamespace
    _ledger_endpoint: BlobEndpoint

class DataCatalog(CatalogNamespace):
    public: _DataCatalogPublicNamespace
    __namespace_list__: list[str]

class _ReportCatalogPublicExamplesBasicsIpynbReport(NotebookEndpoint):
    pass

class _ReportCatalogPublicExamplesNamespace(CatalogNamespace):
    basics_ipynb: _ReportCatalogPublicExamplesBasicsIpynbReport

class _ReportCatalogPublicNamespace(CatalogNamespace):
    examples: _ReportCatalogPublicExamplesNamespace

class ReportCatalog(CatalogNamespace):
    public: _ReportCatalogPublicNamespace
    __namespace_list__: list[str]

datacat: DataCatalog
reportcat: ReportCatalog
