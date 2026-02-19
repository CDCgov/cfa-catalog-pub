import random
import pandas as pd 
import polars as pl 
import pandera.pandas as pa 
from faker import Faker

fake = Faker()

extract_schema = pa.DataFrameSchema(
    {
    "id": pa.Column(int, nullable=False),
    "name": pa.Column(str, nullable=False),
    }
)

load_schema = pa.DataFrameSchema(
    {
    "id": pa.Column(int, nullable=False),
    "name": pa.Column(str, nullable=False),
    }
)

def extract_mock_data(output = "pandas", size = 10) -> pd.DataFrame|pl.DataFrame:
    data = {
        "id": [random.randint(1, 100) for _ in range(size)],
        "name": [fake.name() for _ in range(size)],
    }
    df = pd.DataFrame(data)
    return df if output == "pandas" else pl.from_pandas(df)

def load_mock_data(output = "pandas", size = 10) -> pd.DataFrame|pl.DataFrame:
    data = {
        "id": [random.randint(1, 100) for _ in range(size)],
        "name": [fake.name() for _ in range(size)],
    }
    df = pd.DataFrame(data)
    return df if output == "pandas" else pl.from_pandas(df)