import random

import pandas as pd
import pandera.pandas as pa
import polars as pl
from faker import Faker

fake = Faker()

metric_opts = ["count_ed_visits", "count_admitted_ed_visits", "percent_ed_visits"]
state_opts = ['FL',
 'RI',
 'MO',
 'NJ',
 'CO',
 'NM',
 'VT',
 'MA',
 'MD',
 'WY',
 'UT',
 'ME',
 'SC',
 'WI',
 'TN',
 'NY',
 'MN',
 'IL',
 'IN',
 'LA',
 'MI',
 'TX',
 'DC',
 'CT',
 'ID',
 'GA',
 'SD',
 'AK',
 'WA',
 'WV',
 'VA',
 'NE',
 'IA',
 'PA',
 'NV',
 'OK',
 'AR',
 'OH',
 'OR',
 'DE',
 'KY',
 'MS',
 'ND',
 'NC',
 'NH',
 'KS',
 'GU',
 'HI',
 'AZ',
 'CA',
 'MT',
 'AL']
disease_opts = ['COVID-19/Omicron', 'Total', 'Influenza', 'RSV']

load_schema = pa.DataFrameSchema(
    {
        "report_date": pa.Column(str,
            pa.Check.str_matches(
                r"^\d{4}-\d{2}-\d{2}$"
            ),
            coerce=True,
        ),
        "reference_date": pa.Column(str,
            pa.Check.str_matches(
                r"^\d{4}-\d{2}-\d{2}$"
            ),
            coerce=True,
        ),
        "metric": pa.Column(str, pa.Check.isin(metric_opts), nullable = True),
        "geo_type": pa.Column(str, pa.Check.isin(["state"]), nullable= True),
        "geo_value": pa.Column(str, pa.Check.isin(state_opts), nullable= True),
        "disease": pa.Column(str, pa.Check.isin(disease_opts), nullable= True),
        "value": pa.Column(float, pa.Check.greater_than_or_equal_to(0.0), nullable= True),
    }
)


def load_mock_data(output="pandas", size=10) -> pd.DataFrame | pl.DataFrame:
    df = pd.DataFrame()
    df = df.assign(
        report_date=[fake.date_between(start_date="-1y", end_date="today").isoformat() for _ in range(size)],
        reference_date = [fake.date_between(start_date="-3y", end_date="today").isoformat() for _ in range(size)],
        metric=[random.choice(metric_opts) for _ in range(size)],
        geo_type=["state" for _ in range(size)],
        geo_value=[random.choice(state_opts) for _ in range(size)],
        disease=[random.choice(disease_opts) for _ in range(size)],
        value=[round(random.uniform(0, 25000), 2) for _ in range
    )
    return df if output == "pandas" or output == "pd" else pl.from_pandas(df)