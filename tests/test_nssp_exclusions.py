from datetime import date
from pathlib import Path

import pandera.pandas as pa
import pandas as pd
import polars as pl
import pytest
import tomli

from cfa.catalog.public.datasets.stf.schemas import nssp_exclusions
from cfa.dataops import datacat


def test_catalog_definition_uses_public_defaults() -> None:
    config_path = (
        Path(__file__).parents[1]
        / "cfa/catalog/public/datasets/stf/nssp_exclusions.toml"
    )
    with config_path.open("rb") as config_file:
        config = tomli.load(config_file)

    assert config["properties"] == {
        "name": "nssp_exclusions",
        "type": "reference",
    }
    assert config["load"] == {
        "account": "",
        "container": "",
        "prefix": "dataops/stf/transformed/nssp_exclusions/",
    }


def test_catalog_exposes_load_endpoint_and_mock_data() -> None:
    dataset = datacat.public.stf.nssp_exclusions

    assert dataset.load.account == "cfadatalakeprd"
    assert dataset.load.container == "cfapredict"
    assert dataset.load.prefix == "dataops/stf/transformed/nssp_exclusions"
    assert dataset.load.mock_data(size=2).shape == (2, 3)


def test_mock_data_satisfies_schema_and_includes_empty_review() -> None:
    dataframe = nssp_exclusions.load_mock_data(size=3)

    validated = nssp_exclusions.load_schema.validate(dataframe)

    assert validated.loc[0, "excluded_dates"] == []


def test_polars_fixture_has_persisted_schema_after_parquet_round_trip(
    tmp_path: Path,
) -> None:
    dataframe = nssp_exclusions.load_mock_data(output="polars", size=3)
    parquet_path = tmp_path / "exclusions.parquet"

    dataframe.write_parquet(parquet_path)
    loaded = pl.read_parquet(parquet_path)

    assert loaded.schema == pl.Schema(
        {
            "reference_date": pl.Date,
            "state_abb": pl.String,
            "excluded_dates": pl.List(pl.Date),
        }
    )
    assert loaded["excluded_dates"].to_list()[0] == []
    nssp_exclusions.load_schema.validate(pd.read_parquet(parquet_path))


@pytest.mark.parametrize(
    "excluded_dates",
    [
        [date(2026, 9, 28), date(2026, 9, 27)],
        [date(2026, 9, 28), date(2026, 9, 28)],
        ["2026-09-28"],
    ],
)
def test_schema_rejects_invalid_excluded_dates(excluded_dates: list) -> None:
    dataframe = nssp_exclusions.load_mock_data(size=1)
    dataframe.at[0, "excluded_dates"] = excluded_dates

    with pytest.raises(pa.errors.SchemaError):
        nssp_exclusions.load_schema.validate(dataframe)
