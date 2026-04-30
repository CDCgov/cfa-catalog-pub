# Schemas and Mock Data

## Setting Up Schemas

To make use of schemas (and mock data) in your workflows, you will need a python file with the name matching the dataset. This file will live within a team's `schema` folder in the catalog. For example, suppose we are working with the nhsn_hrd dataset from the stf team that is defined in `datasets/stf/nhsn_hrd.toml`. The path for the associated schema file would be `datasets/stf/schemas/nhsn_hrd.py`.

The schema definitions are built on the pandera.pandas package. it is recommended to import it as `import pandera.pandas as pa`. Then one schema can be created for each stage of data (like extract or load). It's recommended to use the names extract_schema or load_schema for consistency, but any name can be used. Each schema should be created by using `pa.DataFrameSchema()`. See the stf/schemas/nssp_gold_v1.py file for an example.

## Using a Schema

Now that a schema is defined we can use it in code. We can import our new in the following way: `from cfa.catalog.public.datasets.<team>.schemas import <dataset>`. For our specific example we import it as `from cfa.catalog.public.datasets.stf.schemas import nhsn_hrd`. We can then referenced the schemas here like `schema = nhsn_hrd.load_schema`.

Schemas are helpful for ensuring data aligns with expected data columns and column types. Once we have a schema and a dataframe (in pandas format) we can validate the dataframe adheres to the schema in the following way:  
```
schema.validate(df)
```

## Setting Up Mock Data

In the same file as the schema for a dataset, we define how our mock data should be generated. It will be in the form of a function and use either `extract_mock_data` or `load_mock_data` as the name, with the following format:  
```
def load_mock_data(output="pandas", size=10) -> pd.DataFrame | pl.DataFrame:
    df = pd.DataFrame()
    df = df.assign(
        ---
    )
    return df if output == "pandas" or output == "pd" else pl.from_pandas(df)
```

The middle portion of df.assign will be the place to define column names and data generation. This can include random number generation, choosing from options, etc. The general structure for each column is
```
column_name = [random.randint(0,10) for _ in range(size)],
```

Note that column_name is not in quotes.


## Using Mock Data

If datasets have the load_mock_data or extract_mock_data functions defined in their respective schema areas, we can pull this in automatically with cfa-dataops datacat. The mock data functions are accessible at your dataset's load or extract reference endpoint and called `mock_data()`, for example: 
```
ref = datacat.public.stf.nhsn_hrd

extract_df = ref.extract.mock_data()
load_df = ref.load.mock_data()
```

Because of the way we define `extract_mock_data()` and `load_mock_data()` in our schema file, it accepts an `output` parameter of `pandas` or `polars`, and a `size` parameter which is the number of rows in the mock dataframe to generate. For the example above, we can produce a mock dataframe for our load data that is in polars format and 1,000 rows.
```
df = red.load.mock_data(output = "polars", size = 1000)
```