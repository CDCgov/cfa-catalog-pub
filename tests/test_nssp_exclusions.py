from datetime import date, datetime
from pathlib import Path

import pandas as pd
import pandera.pandas as pa
import polars as pl
import pytest

from cfa.catalog.public.datasets.stf.schemas import nssp_exclusions
from cfa.dataops import datacat


def test_catalog_exposes_schema_valid_mock_data() -> None:
    dataset = datacat.public.stf.nssp_exclusions

    assert dataset.load.account == "cfadatalakeprd"
    assert dataset.load.container == "cfapredict"
    assert dataset.load.prefix == "dataops/stf/transformed/nssp_exclusions"

    assert nssp_exclusions.load_schema.validate(
        dataset.load.mock_data(size=0)
    ).empty

    dataframe = dataset.load.mock_data(size=3)
    validated = nssp_exclusions.load_schema.validate(dataframe)

    assert validated.loc[0, "excluded_dates"] == []


def test_polars_fixture_has_persisted_schema_after_parquet_round_trip(
    tmp_path: Path,
) -> None:
    dataframe = nssp_exclusions.load_mock_data(output="polars", size=1)
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


def test_schema_rejects_invalid_excluded_dates() -> None:
    for excluded_dates in (
        [date(2026, 9, 28), date(2026, 9, 27)],
        [date(2026, 9, 28), date(2026, 9, 28)],
        ["2026-09-28"],
        [datetime(2026, 9, 28)],
        [pd.Timestamp("2026-09-28")],
    ):
        dataframe = nssp_exclusions.load_mock_data(size=1)
        dataframe.at[0, "excluded_dates"] = excluded_dates

        with pytest.raises(pa.errors.SchemaError):
            nssp_exclusions.load_schema.validate(dataframe)
