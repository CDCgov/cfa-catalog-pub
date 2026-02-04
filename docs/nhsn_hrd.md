# NHSN HRD Pipeline

## Setup

The NHSN HRD data are separated into two groups in this catalog: nhsn_hrd and nhsn_hrd_prelim.

There are three ways to get the new data into blob storage for cfa-dataops retrieval.

1. use the etl_archive function to pull in data from the archive repo. This intended only to "catch up" on our own archive of the datasets in Blob Storage.
2. run the etl process to store the newest dataset available on data.cdc.gov. This is the intended method for continuing to pull in the newest data using python.
3. run the workflow for the dataset in GitHub Actions with the manual workflow dispatch. This is setup to run automatically every week to pull in new information so that the previous two methods are not necessary.

## GitHub Workflow

There is an internal repo called cfa-dataops-scheduler which is setup to run a workflow weekly to execute the etl pipeline for the prelim and final datasets. The prelim execution kicks off automatically on Wednesday afternoons. The final execution kicks off automatically around midnight on Saturadys. Each workflow pulls data from the data.cdc.gov location and stores the results in Azure Blob Storage. These executions spin up a container app job that processes the etl pipeline.

If you need to run the etl pipeline outside of the automated weekly runs, you can manually kick off the workflow. From the cfa-dataops-scheduler repo, navigate to the Actions tab and select the desired workflow. Then hit `run workflow`.


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
