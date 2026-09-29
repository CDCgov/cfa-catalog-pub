from datetime import date, timedelta
from typing import Literal

import pandas as pd
import pandera.pandas as pa
import polars as pl

STATE_ABBS = (
    "AK",
    "AL",
    "AR",
    "AZ",
    "CA",
    "CO",
    "CT",
    "DC",
    "DE",
    "FL",
    "GA",
    "HI",
    "IA",
    "ID",
    "IL",
    "IN",
    "KS",
    "KY",
    "LA",
    "MA",
    "MD",
    "ME",
    "MI",
    "MN",
    "MO",
    "MS",
    "MT",
    "NC",
    "ND",
    "NE",
    "NH",
    "NJ",
    "NM",
    "NV",
    "NY",
    "OH",
    "OK",
    "OR",
    "PA",
    "RI",
    "SC",
    "SD",
    "TN",
    "TX",
    "US",
    "UT",
    "VA",
    "VT",
    "WA",
    "WI",
    "WV",
    "WY",
)


def _is_sorted_date_sequence(value: object) -> bool:
    if isinstance(value, (str, bytes)):
        return False
    try:
        values = list(value)  # type: ignore[arg-type]
    except TypeError:
        return False
    return all(isinstance(item, date) for item in values) and values == sorted(
        set(values)
    )


load_schema = pa.DataFrameSchema(
    {
        "reference_date": pa.Column(pa.Date, coerce=True),
        "state_abb": pa.Column(str, pa.Check.isin(STATE_ABBS)),
        "excluded_dates": pa.Column(
            object,
            pa.Check(_is_sorted_date_sequence, element_wise=True),
        ),
    },
    unique=["reference_date", "state_abb"],
    strict=True,
)


def load_mock_data(
    output: Literal["pandas", "pd", "polars", "pl"] = "pandas",
    size: int = 10,
) -> pd.DataFrame | pl.DataFrame:
    """Create deterministic, schema-valid reviewed-exclusion rows."""
    if size < 0:
        raise ValueError("size must be nonnegative")
    if size > len(STATE_ABBS):
        raise ValueError(f"size must not exceed {len(STATE_ABBS)}")
    if output not in {"pandas", "pd", "polars", "pl"}:
        raise ValueError("output must be 'pandas', 'pd', 'polars', or 'pl'")

    reference_date = date(2026, 9, 29)
    data = {
        "reference_date": [reference_date] * size,
        "state_abb": list(STATE_ABBS[:size]),
        "excluded_dates": [
            [] if index == 0 else [reference_date - timedelta(days=1)]
            for index in range(size)
        ],
    }
    pandas_df = pd.DataFrame(data)
    return (
        pandas_df if output in {"pandas", "pd"} else pl.from_pandas(pandas_df)
    )
