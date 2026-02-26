import random
import pandas as pd 
import polars as pl 
import pandera.pandas as pa 
from faker import Faker

fake = Faker()

geo_list = ['AK', 'AL', 'AR', 'AZ', 'CA', 'CO', 'CT', 'DC', 'DE', 'FL',
       'GA', 'GU', 'HI', 'IA', 'ID', 'IL', 'IN', 'KS', 'KY', 'LA', 'MA',
       'MD', 'ME', 'MI', 'MN', 'MO', 'MS', 'MT', 'NC', 'ND', 'NE', 'NH',
       'NJ', 'NM', 'NV', 'NY', 'OH', 'OK', 'OR', 'PA', 'RI', 'SC', 'SD',
       'TN', 'TX', 'US', 'UT', 'VA', 'VT', 'WA', 'WI', 'WV', 'WY']

load_schema = pa.DataFrameSchema(
    columns={
        "id": pa.Column('int32', pa.Check(lambda x: x >= 3)),
        "start_date": pa.Column(object, pa.Check(lambda x: pd.to_datetime(x, errors='coerce').notna()), nullable = True),  # Check if start_date can be converted to datetime
        "end_date": pa.Column(object, pa.Check(lambda x: pd.to_datetime(x, errors='coerce').notna()), nullable = True),  # Check if end_date can be converted to datetime
        "disease": pa.Column(str, pa.Check.isin(["COVID-19", "Influenza", "RSV"])),
        "parameter": pa.Column(str, pa.Check.isin(['delay', 'right_truncation', 'generation_interval'])),
        "format": pa.Column(str, pa.Check.equal_to("PMF")),
        "geo_value": pa.Column(str, pa.Check.isin(geo_list), nullable = True),
        "reference_date": pa.Column(object, pa.Check(lambda x: pd.to_datetime(x, errors='coerce').notna()), nullable = True),
        "value": pa.Column(object, pa.Check(lambda x: x.apply(lambda arr: all(0 <= i <= 1 for i in arr) and sum(arr) <= 1.01)), nullable = True),  # Check if value is a list of numbers between 0 and 1
    }
)


def load_mock_data(output = "pandas", size = 10) -> pd.DataFrame|pl.DataFrame:
    df = pd.DataFrame()
    df = df.assign(
        id = range(3, 3 + size),
        start_date = pd.date_range(start='2023-07-01', periods=size),
        end_date = pd.date_range(start='2024-07-01', periods=size),
        disease = random.choices(["COVID-19", "Influenza", "RSV"], k=size),
        parameter = random.choices(['delay', 'right_truncation', 'generation_interval'], k=size),
        format = ["PMF"] * size,
        geo_value = random.choices(geo_list, k=size),
        reference_date = pd.date_range(start='2023-07-01', periods=size),
        value = [[0.1, 0.2, 0.3, 0.4]] * size
    )
    return df if output == "pandas" or output == "pd" else pl.from_pandas(df)
