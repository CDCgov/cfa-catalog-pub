# CFA Catalog: Public (CDCgov)

## Overview

The CFA Catalog: Public (CDCgov) is a comprehensive data management and analysis platform designed for the CDC's Center for Forecasting and Analytics (CFA). It serves as the organizational layer on top of the CFA dataOps framework, enabling teams to standardize how data assets are described, discovered, and used across projects. This catalog provides a structured framework for managing datasets, workflows, modeling components, and reports related to public health data analysis and forecasting.

### How It Works
The catalog is implemented as a collection of configuration-driven definitions that describe how datasets are ingested, transformed, validated, and exposed. Each dataset is defined using structured configuration (e.g. TOML), along with associated schema definitions and transformation logic.

### Key Components

- **Datasets**: Curated collection of public health datasets with standardized ETL configurations
- **Workflows**: Automated data processing pipelines for various analytical tasks
- **Reports**: Parameterizable Jupyter notebooks for generating analytical reports

### Architecture

The catalog is built on the `cfa-dataops` framework and provides:

- **ETL Pipeline Management**: Extract, Transform, Load operations for various data sources
- **Schema Validation**: Data quality assurance using Pandera schemas
- **Cloud Storage Integration**: Azure Blob Storage integration for scalable data storage
- **Workflow Automation**: Configurable workflows for complex data processing tasks
- **Report Generation**: Automated report creation with parameterizable notebooks
- **Multi-Catalog Support**: This catalog can be installed alongside other catalogs, with all namespaces co-located in the `datacat` and `reportcat` objects for unified access

### Available Datasets

- **reference**
  - `cenpop2020`: Census Population 2020
  - `state_hhs_regions`: State, HHS, FIPS data

- **stf**
  - `comprehensive_nssp_gold`
  - `nhsn_hrd_prelim`
  - `nhsn_hrd`
  - `nssp_gold_v1`
  - `nssp_gold_v2`
  - `nwss`
  - `param_estimates`

### How It Integrates with CFA DataOps
The CFA Data Catalog is tightly coupled with the CFA DataOps framework and functions as its primary interface for dataset definition and discovery.

CFA DataOps provides the execution layer, while the catalog provides the declaratie layer.

  **CFA DataOps Responsibilities**
  - Executes ETL pipelines defined in the catalog
  - Manages schema validation and mock data generation
  - Handles data versioning and storage in Azure Blob Storage
  - Provides utilities for accessing datasets and APIs (e.g. Socrata)

  **CFA Catalog Responsibilities**
  - Defines dataset structure, transformations, adn schemas
  - Organizes workflows and reporting artifacts
  - Serves as the entry point for users interacting with data assets.

In practice, this integration enables a configuration-driven workflow:
  1.  A dataset is defined in the catalog with its schema and transformation logic.
  2.  CFA DataOps reads the catalog definition and executes the corresponding pipeline.
  3.  Data is validated, transformed, and stored in Azure Blob Storage with versioning.
  4.  Downstream users access the dataset via standardized interfaces or generat reports using reportcat.

Recent enhancements further strengthen this integration, including:
  - LazyFrame loading in Polars for efficient data access without immediate materialization.
  - Automated schema and mock data generation directly from catalog definitions.
  - Migration toward Dagster for mor robust orchestration and scheduling.

Together, the catalog and CFA DataOps create a unified system where daa engineering is reproducible, discoverable, and scalable.

### Getting Started
New users can begin working with CFA Data Catalog by following these steps:
1. Explore the Catalog
   Review available datasets, schemas, and workflows defined in the catalog repository.
2. Access Data via CFA DataOps
   Use CFA DataOps utilities to load datasets into your analysis environment. Data can be queried using DuckDB or Polars without requiring external database infrastructure.
3. Run or Extend Pipelines
   Execute existing ETL workflows or define new ones using catalog templates and configuration files.

4. Validate and Test
   Leverage built-in schema validation and mock data generation to ensure correctness during development

5. Generate Outputs
   Use parameterized notebooks to produce reports, dashboards, or model inputs in a reproducible manner.

By adhering to catalog standards and leveraging CFA DataOps tooling, users can quickly onboard to existing data assets and contribute new datasets in a consistent, production-ready manner.

## Project admins

- Phillip Rogers <ap66@cdc.gov> (CDC/OD/ORR/CFA)(CTR)
- Ryan Raasch <xng3@cdc.gov> (CDC/OD/ORR/CFA)(CTR)

---

## Disclaimers

### General Disclaimer

This repository was created for use by CDC programs to collaborate on public health related projects in support of the [CDC mission](https://www.cdc.gov/about/organization/mission.htm). GitHub is not hosted by the CDC, but is a third party website used by CDC and its partners to share information and collaborate on software. CDC use of GitHub does not imply an endorsement of any one particular service, product, or enterprise.

### Public Domain Standard Notice

This repository constitutes a work of the United States Government and is not subject to domestic copyright protection under 17 USC § 105. This repository is in the public domain within the United States, and copyright and related rights in the work worldwide are waived through the [CC0 1.0 Universal public domain dedication](https://creativecommons.org/publicdomain/zero/1.0/). All contributions to this repository will be released under the CC0 dedication. By submitting a pull request you are agreeing to comply with this waiver of copyright interest.

### License Standard Notice

This repository is licensed under ASL v2 or later.

This source code in this repository is free: you can redistribute it and/or modify it under the terms of the Apache Software License version 2, or (at your option) any later version.

This source code in this repository is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the Apache Software License for more details.

You should have received a copy of the Apache Software License along with this program. If not, see http://www.apache.org/licenses/LICENSE-2.0.html

The source code forked from other open source projects will inherit its license.

### Privacy Standard Notice

This repository contains only non-sensitive, publicly available data and information. All material and community participation is covered by the [Disclaimer](https://github.com/CDCgov/template/blob/master/DISCLAIMER.md) and [Code of Conduct](https://github.com/CDCgov/template/blob/master/code-of-conduct.md). For more information about CDC's privacy policy, please visit [http://www.cdc.gov/other/privacy.html](https://www.cdc.gov/other/privacy.html).

### Contributing Standard Notice

Anyone is encouraged to contribute to the repository by [forking](https://help.github.com/articles/fork-a-repo) and submitting a pull request. (If you are new to GitHub, you might start with a [basic tutorial](https://help.github.com/articles/set-up-git).) By contributing to this project, you grant a world-wide, royalty-free, perpetual, irrevocable, non-exclusive, transferable license to all users under the terms of the [Apache Software License v2](http://www.apache.org/licenses/LICENSE-2.0.html) or later.

All comments, messages, pull requests, and other submissions received through CDC including this GitHub page may be subject to applicable federal law, including but not limited to the Federal Records Act, and may be archived. Learn more at [http://www.cdc.gov/other/privacy.html](http://www.cdc.gov/other/privacy.html).

### Records Management Standard Notice

This repository is not a source of government records but is a copy to increase collaboration and collaborative potential. All government records will be published through the [CDC web site](http://www.cdc.gov).
