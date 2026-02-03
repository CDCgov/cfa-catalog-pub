# NHSN HRD Pipeline

## Setup

The NHSN HRD data are separated into two groups in this catalog: nhsn_hrd and nhsn_hrd_prelim.

There are two ways to get the new data into blob storage for cfa-dataops retrieval.

1. use the etl_archive function to pull in data from the archive repo. This intended only to "catch up" on our own archive of the datasets in Blob storage.
2. run the etl process to store the newest dataset available on data.cdc.gov. This is the intended method for continuing to pull in the newest data.

## Pull files from archive repo

```python
# import
from cfa.catalog.public.workflows.etl.stf import nhsn_hrd, nhsn_hrd_prelim

#kick off the archive for the final version
nhsn_hrd.etl_archive()

#kick off the archive for the prelim version
nhsn_hrd_prelim.etl_archive()
```

## Run ETL

```python
# import
from cfa.catalog.public.workflows.etl.stf import nhsn_hrd, nhsn_hrd_prelim

# run etl for nhsn_hrd
raw = nhsn_hrd.extract()
data_t = nhsn_hrd.transform(raw)
nhsn_hrd.load(data_t)

# run etl for nhsn_hrd_prelim
raw = nhsn_hrd_prelim.extract()
data_t = nhsn_hrd_prelim.transform(raw)
nhsn_hrd_prelim.load(data_t)
```

## Accessing the transformed data

```python
# import
from cfa.dataops import datacat

# assign the namespace for easier access
dataset = datacat.public.stf.nhsn_hrd
dataset_prelim = datacat.public.stf.nhsn_hrd_prelim

# get the "load" (transformed) datasets
df = dataset.load.get_dataframe()
df_prelim = dataset_prelim.load.get_dataframe()

```
