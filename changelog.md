# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Calendar Versioning](https://calver.org/).
The versioning pattern is `YYYY.MM.DD.micro

---

# [2025.10.06.0]

## Added

- Initialized git repo with this new catalog
- Created first dataset: `public.stf.nssp_gold.toml`
    - Console command `stf_nssp_gold_copy` can be use to run update in CICD.
- Added etl workflow for making redundant copy of nssp_gold into a dataops compatible blob path

## Example

```python
>>> from cfa.dataops import datacat
>>> dataset = datacat.public.stf.nssp_gold
>>> df = dataset.load.get_dataframe(output='pl', version='latest')
>>> df.head()
```

```bash
$ stf_nssp_gold_copy
No new files to copy
```
