import random

import pandas as pd
import pandera.pandas as pa
import polars as pl
from faker import Faker

fake = Faker()

metric_opts = [
    "count_ed_visits",
    "percent_ed_visits",
    "count_admitted_ed_visits",
]
geo_value_opts = [
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
    "GU",
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
    "UT",
    "VA",
    "VT",
    "WA",
    "WI",
    "WV",
    "WY",
]
disease_opts = ["COVID-19/Omicron", "RSV", "Influenza", "Total"]

load_schema = pa.DataFrameSchema(
    {
        "report_date": pa.Column(
            str,
            pa.Check.str_matches(
                r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}(\.\d{3})?$"
            ),
            coerce=True,
        ),  # Check if report_date can be converted to datetime
        "reference_date": pa.Column(
            str, pa.Check(lambda x: pd.to_datetime(x, errors="coerce").notna())
        ),  # Check if reference_date can be converted to datetime
        "asof": pa.Column(
            str, pa.Check(lambda x: pd.to_datetime(x, errors="coerce").notna())
        ),  # Check if asof can be converted to datetime
        "facility": pa.Column(
            int, pa.Check(lambda x: x >= 0)
        ),  # Check if facility is a non-negative integer
        "metric": pa.Column(
            str, pa.Check.isin(metric_opts)
        ),  # Check if metric is one of the predefined options
        "geo_type": pa.Column(
            str, pa.Check.isin(["state"])
        ),  # Check if geo_type is a non-empty string
        "geo_value": pa.Column(
            str, pa.Check.isin(geo_value_opts)
        ),  # Check if geo_value is one of the predefined options
        "run_id": pa.Column(
            str
        ),  # Check if run_id is one of the predefined options
        "disease": pa.Column(
            str, pa.Check.isin(disease_opts)
        ),  # Check if disease is one of the predefined options
        "value": pa.Column(
            float, pa.Check(lambda x: x >= 0)
        ),  # Check if value is a non-negative float
    }
)


def load_mock_data(output="pandas", size=10) -> pd.DataFrame | pl.DataFrame:
    df = pd.DataFrame()
    df = df.assign(
        report_date=["2026-02-02"] * size,
        reference_date=["2023-07-01"] * size,
        asof=["2026-02-02"] * size,
        facility=[random.randint(1237, 35720) for _ in range(size)],
        metric=random.choices(metric_opts, k=size),
        geo_type=["state"] * size,
        geo_value=random.choices(geo_value_opts, k=size),
        run_id=["598084b2-5f3a-4d07-b473-b7903ed7e669" for _ in range(size)],
        disease=random.choices(disease_opts, k=size),
        value=[random.uniform(0, 30000) for _ in range(size)],
    )
    return df if output == "pandas" or output == "pd" else pl.from_pandas(df)
