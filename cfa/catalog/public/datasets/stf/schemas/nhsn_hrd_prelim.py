import random

import pandas as pd
import pandera.pandas as pa
import polars as pl
from faker import Faker

fake = Faker()

region_opts = [
    "AL",
    "AR",
    "AS",
    "AZ",
    "CA",
    "CO",
    "CT",
    "DC",
    "DE",
    "FL",
    "GU",
    "HI",
    "IL",
    "IN",
    "KS",
    "ME",
    "MN",
    "MP",
    "MS",
    "MT",
    "NE",
    "NH",
    "OH",
    "OK",
    "PA",
    "PR",
    "RI",
    "Region 10",
    "Region 2",
    "Region 4",
    "Region 6",
    "Region 7",
    "SC",
    "SD",
    "TN",
    "USA",
    "WI",
    "ID",
    "LA",
    "MD",
    "NJ",
    "NM",
    "OR",
    "Region 8",
    "VT",
    "WA",
    "AK",
    "GA",
    "MO",
    "NV",
    "Region 5",
    "Region 9",
    "UT",
    "KY",
    "MA",
    "MI",
    "NC",
    "Region 1",
    "TX",
    "WY",
    "Region 3",
    "VA",
    "VI",
    "WV",
    "NY",
    "IA",
    "ND",
]


extract_schema = pa.DataFrameSchema(
    {
        "weekendingdate": pa.Column(object, nullable=True, coerce=True),
        "jurisdiction": pa.Column(
            str, pa.Check.isin(region_opts), nullable=True, coerce=True
        ),
        "numinptbeds": pa.Column(float, nullable=True, coerce=True),
        "numinptbedsadult": pa.Column(float, nullable=True, coerce=True),
        "numinptbedsped": pa.Column(float, nullable=True, coerce=True),
        "numinptbedsocc": pa.Column(float, nullable=True, coerce=True),
        "numinptbedsoccadult": pa.Column(float, nullable=True, coerce=True),
        "numinptbedsoccped": pa.Column(float, nullable=True, coerce=True),
        "numicubeds": pa.Column(float, nullable=True, coerce=True),
        "numicubedsadult": pa.Column(float, nullable=True, coerce=True),
        "numicubedsped": pa.Column(float, nullable=True, coerce=True),
        "numicubedsocc": pa.Column(float, nullable=True, coerce=True),
        "numicubedsoccadult": pa.Column(float, nullable=True, coerce=True),
        "numicubedsoccped": pa.Column(float, nullable=True, coerce=True),
        "numconfc19hosppatsadult": pa.Column(
            float, nullable=True, coerce=True
        ),
        "numconfc19hosppatsped": pa.Column(float, nullable=True, coerce=True),
        "totalconfc19hosppats": pa.Column(float, nullable=True, coerce=True),
        "totalconffluhosppats": pa.Column(float, nullable=True, coerce=True),
        "numconfc19icupatsadult": pa.Column(float, nullable=True, coerce=True),
        "totalconfc19icupats": pa.Column(float, nullable=True, coerce=True),
        "totalconffluicupats": pa.Column(float, nullable=True, coerce=True),
        "totalconfc19newadmped": pa.Column(float, nullable=True, coerce=True),
        "numconfc19newadmadult18to49": pa.Column(
            float, nullable=True, coerce=True
        ),
        "totalconfc19newadmadult": pa.Column(
            float, nullable=True, coerce=True
        ),
        "numconfc19newadmunk": pa.Column(float, nullable=True, coerce=True),
        "totalconfc19newadm": pa.Column(float, nullable=True, coerce=True),
        "totalconfflunewadm": pa.Column(float, nullable=True, coerce=True),
        "pctinptbedsocc": pa.Column(float, nullable=True, coerce=True),
        "pctconfc19inptbeds": pa.Column(float, nullable=True, coerce=True),
        "pctconffluinptbeds": pa.Column(float, nullable=True, coerce=True),
        "pcticubedsocc": pa.Column(float, nullable=True, coerce=True),
        "pctconfc19icubeds": pa.Column(float, nullable=True, coerce=True),
        "pctconffluicubeds": pa.Column(float, nullable=True, coerce=True),
        "pctconfc19newadmadult": pa.Column(float, nullable=True, coerce=True),
        "pctconfc19newadmped": pa.Column(float, nullable=True, coerce=True),
        "numinptbedshosprep": pa.Column(float, nullable=True, coerce=True),
        "numinptbedsocchosprep": pa.Column(float, nullable=True, coerce=True),
        "numicubedshosprep": pa.Column(float, nullable=True, coerce=True),
        "numicubedsocchosprep": pa.Column(float, nullable=True, coerce=True),
        "totalconfc19hosppatshosprep": pa.Column(
            float, nullable=True, coerce=True
        ),
        "totalconffluhosppatshosprep": pa.Column(
            float, nullable=True, coerce=True
        ),
        "totalconfrsvhosppatshosprep": pa.Column(
            float, nullable=True, coerce=True
        ),
        "totalconfc19icupatshosprep": pa.Column(
            float, nullable=True, coerce=True
        ),
        "totalconffluicupatshosprep": pa.Column(
            float, nullable=True, coerce=True
        ),
        "totalconfrsvicupatshosprep": pa.Column(
            float, nullable=True, coerce=True
        ),
        "totalconfc19newadmpedhosprep": pa.Column(
            float, nullable=True, coerce=True
        ),
        "totalconfc19newadmadulthosprep": pa.Column(
            float, nullable=True, coerce=True
        ),
        "totalconfc19newadmhosprep": pa.Column(
            float, nullable=True, coerce=True
        ),
        "totalconfflunewadmpedhosprep": pa.Column(
            float, nullable=True, coerce=True
        ),
        "totalconfflunewadmadulthosprep": pa.Column(
            float, nullable=True, coerce=True
        ),
        "totalconfflunewadmhosprep": pa.Column(
            float, nullable=True, coerce=True
        ),
        "totalconfrsvnewadmpedhosprep": pa.Column(
            float, nullable=True, coerce=True
        ),
        "totalconfrsvnewadmadulthosprep": pa.Column(
            float, nullable=True, coerce=True
        ),
        "totalconfrsvnewadmhosprep": pa.Column(
            float, nullable=True, coerce=True
        ),
        "pctinptbedsocchosprep": pa.Column(float, nullable=True, coerce=True),
        "pcticubedsocchosprep": pa.Column(float, nullable=True, coerce=True),
        "pctconfc19inptbedshosprep": pa.Column(
            float, nullable=True, coerce=True
        ),
        "pctconffluinptbedshosprep": pa.Column(
            float, nullable=True, coerce=True
        ),
        "pctconfrsvinptbedshosprep": pa.Column(
            float, nullable=True, coerce=True
        ),
        "pctconfc19icubedshosprep": pa.Column(
            float, nullable=True, coerce=True
        ),
        "pctconffluicubedshosprep": pa.Column(
            float, nullable=True, coerce=True
        ),
        "pctconfrsvicubedshosprep": pa.Column(
            float, nullable=True, coerce=True
        ),
        "numinptbedsperchosprep": pa.Column(float, nullable=True, coerce=True),
        "numinptbedsoccperchosprep": pa.Column(
            float, nullable=True, coerce=True
        ),
        "numicubedsperchosprep": pa.Column(float, nullable=True, coerce=True),
        "numicubedsoccperchosprep": pa.Column(
            float, nullable=True, coerce=True
        ),
        "totalconfc19hosppatsperc": pa.Column(
            float, nullable=True, coerce=True
        ),
        "totalconffluhosppatsperc": pa.Column(
            float, nullable=True, coerce=True
        ),
        "totalconfrsvhosppatsperc": pa.Column(
            float, nullable=True, coerce=True
        ),
        "totalconfc19icupatsperchosprep": pa.Column(
            float, nullable=True, coerce=True
        ),
        "totalconffluicupatsperchosprep": pa.Column(
            float, nullable=True, coerce=True
        ),
        "totalconfrsvicupatsperchosprep": pa.Column(
            float, nullable=True, coerce=True
        ),
        "totalconfc19newadmpedper": pa.Column(
            float, nullable=True, coerce=True
        ),
        "totalconfc19newadmadultp": pa.Column(
            float, nullable=True, coerce=True
        ),
        "totalconfc19newadmperchosprep": pa.Column(
            float, nullable=True, coerce=True
        ),
        "totalconfflunewadmpedper": pa.Column(
            float, nullable=True, coerce=True
        ),
        "totalconfflunewadmadultp": pa.Column(
            float, nullable=True, coerce=True
        ),
        "totalconfflunewadmperchosprep": pa.Column(
            float, nullable=True, coerce=True
        ),
        "totalconfrsvnewadmpedper": pa.Column(
            float, nullable=True, coerce=True
        ),
        "totalconfrsvnewadmadultp": pa.Column(
            float, nullable=True, coerce=True
        ),
        "totalconfrsvnewadmperchosprep": pa.Column(
            float, nullable=True, coerce=True
        ),
        "pctinptbedsoccperchosprep": pa.Column(
            float, nullable=True, coerce=True
        ),
        "pcticubedsoccperchosprep": pa.Column(
            float, nullable=True, coerce=True
        ),
        "pctconfc19inptbedsperchosprep": pa.Column(
            float, nullable=True, coerce=True
        ),
        "pctconffluinptbedsperchosprep": pa.Column(
            float, nullable=True, coerce=True
        ),
        "pctconfrsvinptbedsperchosprep": pa.Column(
            float, nullable=True, coerce=True
        ),
        "pctconfc19icubedsperchosprep": pa.Column(
            float, nullable=True, coerce=True
        ),
        "pctconffluicubedsperchosprep": pa.Column(
            float, nullable=True, coerce=True
        ),
        "pctconfrsvicubedsperchosprep": pa.Column(
            float, nullable=True, coerce=True
        ),
        "numinptbedsperchosprepabschg": pa.Column(
            float, nullable=True, coerce=True
        ),
        "numinptbedsoccperchospre": pa.Column(
            float, nullable=True, coerce=True
        ),
        "numicubedsperchosprepabschg": pa.Column(
            float, nullable=True, coerce=True
        ),
        "numicubedsoccperchosprepabschg": pa.Column(
            float, nullable=True, coerce=True
        ),
        "totalconfc19hosppatsperc_1": pa.Column(
            float, nullable=True, coerce=True
        ),
        "totalconffluhosppatsperc_1": pa.Column(
            float, nullable=True, coerce=True
        ),
        "totalconfrsvhosppatsperc_1": pa.Column(
            float, nullable=True, coerce=True
        ),
        "totalconfc19icupatsperch": pa.Column(
            float, nullable=True, coerce=True
        ),
        "totalconffluicupatsperch": pa.Column(
            float, nullable=True, coerce=True
        ),
        "totalconfrsvicupatsperch": pa.Column(
            float, nullable=True, coerce=True
        ),
        "totalconfc19newadmpedper_1": pa.Column(
            float, nullable=True, coerce=True
        ),
        "totalconfc19newadmadultp_1": pa.Column(
            float, nullable=True, coerce=True
        ),
        "totalconfc19newadmpercho": pa.Column(
            float, nullable=True, coerce=True
        ),
        "totalconfflunewadmpedper_1": pa.Column(
            float, nullable=True, coerce=True
        ),
        "totalconfflunewadmadultp_1": pa.Column(
            float, nullable=True, coerce=True
        ),
        "totalconfflunewadmpercho": pa.Column(
            float, nullable=True, coerce=True
        ),
        "totalconfrsvnewadmpedper_1": pa.Column(
            float, nullable=True, coerce=True
        ),
        "totalconfrsvnewadmadultp_1": pa.Column(
            float, nullable=True, coerce=True
        ),
        "totalconfrsvnewadmpercho": pa.Column(
            float, nullable=True, coerce=True
        ),
        "pctinptbedsoccperchospre": pa.Column(
            float, nullable=True, coerce=True
        ),
        "pcticubedsoccperchosprepabschg": pa.Column(
            float, nullable=True, coerce=True
        ),
        "pctconfc19inptbedspercho": pa.Column(
            float, nullable=True, coerce=True
        ),
        "pctconffluinptbedspercho": pa.Column(
            float, nullable=True, coerce=True
        ),
        "pctconfrsvinptbedspercho": pa.Column(
            float, nullable=True, coerce=True
        ),
        "pctconfc19icubedsperchos": pa.Column(
            float, nullable=True, coerce=True
        ),
        "pctconffluicubedsperchos": pa.Column(
            float, nullable=True, coerce=True
        ),
        "pctconfrsvicubedsperchos": pa.Column(
            float, nullable=True, coerce=True
        ),
        "totalconfc19newadmpedper100k": pa.Column(
            float, nullable=True, coerce=True
        ),
        "numconfc19newadmadult18to49per100k": pa.Column(
            float, nullable=True, coerce=True
        ),
        "totalconfc19newadmadultper100k": pa.Column(
            float, nullable=True, coerce=True
        ),
        "totalconfc19newadmper100k": pa.Column(
            float, nullable=True, coerce=True
        ),
        "totalconfflunewadmper100k": pa.Column(
            float, nullable=True, coerce=True
        ),
        "totalconfc19newadmperchosprepabove80pct": pa.Column(
            float, nullable=True, coerce=True
        ),
        "totalconfc19newadmperchosprepabove90pct": pa.Column(
            float, nullable=True, coerce=True
        ),
        "totalconfflunewadmperchosprepabove80pct": pa.Column(
            float, nullable=True, coerce=True
        ),
        "totalconfflunewadmperchosprepabove90pct": pa.Column(
            float, nullable=True, coerce=True
        ),
        "totalconfrsvnewadmperchosprepabove80pct": pa.Column(
            float, nullable=True, coerce=True
        ),
        "totalconfrsvnewadmperchosprepabove90pct": pa.Column(
            float, nullable=True, coerce=True
        ),
        "pctinptbedsoccadult": pa.Column(float, nullable=True, coerce=True),
        "pctinptbedsoccped": pa.Column(float, nullable=True, coerce=True),
        "pcticubedsoccadult": pa.Column(float, nullable=True, coerce=True),
        "pcticubedsoccped": pa.Column(float, nullable=True, coerce=True),
        "pctconfc19inptbedsadult": pa.Column(
            float, nullable=True, coerce=True
        ),
        "pctconfc19inptbedsped": pa.Column(float, nullable=True, coerce=True),
        "pctconfc19icubedsadult": pa.Column(float, nullable=True, coerce=True),
        "pctconfc19hosppatsicu": pa.Column(float, nullable=True, coerce=True),
        "pctconfc19hosppatsicuadult": pa.Column(
            float, nullable=True, coerce=True
        ),
        "pctconffluhosppatsicu": pa.Column(float, nullable=True, coerce=True),
        "totalconfc19newadmpedpctchg": pa.Column(
            float, nullable=True, coerce=True
        ),
        "numconfc19newadmadult18to49pctchg": pa.Column(
            float, nullable=True, coerce=True
        ),
        "totalconfc19newadmadultpctchg": pa.Column(
            float, nullable=True, coerce=True
        ),
        "totalconfc19newadmpctchg": pa.Column(
            float, nullable=True, coerce=True
        ),
        "totalconfflunewadmpctchg": pa.Column(
            float, nullable=True, coerce=True
        ),
        "pctinptbedsoccadulthosprep": pa.Column(
            float, nullable=True, coerce=True
        ),
        "pctinptbedsoccpedhosprep": pa.Column(
            float, nullable=True, coerce=True
        ),
        "pcticubedsoccadulthosprep": pa.Column(
            float, nullable=True, coerce=True
        ),
        "pcticubedsoccpedhosprep": pa.Column(
            float, nullable=True, coerce=True
        ),
        "pctconfc19inptbedsadulthosprep": pa.Column(
            float, nullable=True, coerce=True
        ),
        "pctconfc19inptbedspedhosprep": pa.Column(
            float, nullable=True, coerce=True
        ),
        "pctconfc19icubedsadulthosprep": pa.Column(
            float, nullable=True, coerce=True
        ),
        "pctconfc19icubedspedhosprep": pa.Column(
            float, nullable=True, coerce=True
        ),
        "pctconffluinptbedsadulthosprep": pa.Column(
            float, nullable=True, coerce=True
        ),
        "pctconffluinptbedspedhosprep": pa.Column(
            float, nullable=True, coerce=True
        ),
        "pctconffluicubedsadulthosprep": pa.Column(
            float, nullable=True, coerce=True
        ),
        "pctconffluicubedspedhosprep": pa.Column(
            float, nullable=True, coerce=True
        ),
        "pctconfrsvinptbedsadulthosprep": pa.Column(
            float, nullable=True, coerce=True
        ),
        "pctconfrsvinptbedspedhosprep": pa.Column(
            float, nullable=True, coerce=True
        ),
        "pctconfrsvicubedsadulthosprep": pa.Column(
            float, nullable=True, coerce=True
        ),
        "pctconfrsvicubedspedhosprep": pa.Column(
            float, nullable=True, coerce=True
        ),
        "pctconfc19hosppatsicuhosprep": pa.Column(
            float, nullable=True, coerce=True
        ),
        "pctconfc19hosppatsicuadulthosprep": pa.Column(
            float, nullable=True, coerce=True
        ),
        "pctconfc19hosppatsicupedhosprep": pa.Column(
            float, nullable=True, coerce=True
        ),
        "pctconffluhosppatsicuhosprep": pa.Column(
            float, nullable=True, coerce=True
        ),
        "pctconffluhosppatsicuadulthosprep": pa.Column(
            float, nullable=True, coerce=True
        ),
        "pctconffluhosppatsicupedhosprep": pa.Column(
            float, nullable=True, coerce=True
        ),
        "pctconfrsvhosppatsicuhosprep": pa.Column(
            float, nullable=True, coerce=True
        ),
        "pctconfrsvhosppatsicuadulthosprep": pa.Column(
            float, nullable=True, coerce=True
        ),
        "pctconfrsvhosppatsicupedhosprep": pa.Column(
            float, nullable=True, coerce=True
        ),
        "pctinptbedsoccadultperchosprep": pa.Column(
            float, nullable=True, coerce=True
        ),
        "pctinptbedsoccpedperchosprep": pa.Column(
            float, nullable=True, coerce=True
        ),
        "pcticubedsoccadultperchosprep": pa.Column(
            float, nullable=True, coerce=True
        ),
        "pcticubedsoccpedperchosprep": pa.Column(
            float, nullable=True, coerce=True
        ),
        "pctconfc19inptbedsadultperchosprep": pa.Column(
            float, nullable=True, coerce=True
        ),
        "pctconfc19inptbedspedperchosprep": pa.Column(
            float, nullable=True, coerce=True
        ),
        "pctconfc19icubedsadultperchosprep": pa.Column(
            float, nullable=True, coerce=True
        ),
        "pctconfc19icubedspedperchosprep": pa.Column(
            float, nullable=True, coerce=True
        ),
        "pctconffluinptbedsadultperchosprep": pa.Column(
            float, nullable=True, coerce=True
        ),
        "pctconffluinptbedspedperchosprep": pa.Column(
            float, nullable=True, coerce=True
        ),
        "pctconffluicubedsadultperchosprep": pa.Column(
            float, nullable=True, coerce=True
        ),
        "pctconffluicubedspedperchosprep": pa.Column(
            float, nullable=True, coerce=True
        ),
        "pctconfrsvinptbedsadultperchosprep": pa.Column(
            float, nullable=True, coerce=True
        ),
        "pctconfrsvinptbedspedperchosprep": pa.Column(
            float, nullable=True, coerce=True
        ),
        "pctconfrsvicubedsadultperchosprep": pa.Column(
            float, nullable=True, coerce=True
        ),
        "pctconfrsvicubedspedperchosprep": pa.Column(
            float, nullable=True, coerce=True
        ),
        "pctconfc19hosppatsicuperchosprep": pa.Column(
            float, nullable=True, coerce=True
        ),
        "pctconfc19hosppatsicuadultperchosprep": pa.Column(
            float, nullable=True, coerce=True
        ),
        "pctconfc19hosppatsicupedperchosprep": pa.Column(
            float, nullable=True, coerce=True
        ),
        "pctconffluhosppatsicuperchosprep": pa.Column(
            float, nullable=True, coerce=True
        ),
        "pctconffluhosppatsicuadultperchosprep": pa.Column(
            float, nullable=True, coerce=True
        ),
        "pctconffluhosppatsicupedperchosprep": pa.Column(
            float, nullable=True, coerce=True
        ),
        "pctconfrsvhosppatsicuperchosprep": pa.Column(
            float, nullable=True, coerce=True
        ),
        "pctconfrsvhosppatsicuadultperchosprep": pa.Column(
            float, nullable=True, coerce=True
        ),
        "pctconfrsvhosppatsicupedperchosprep": pa.Column(
            float, nullable=True, coerce=True
        ),
        "pctinptbedsoccadultperchosprepabschg": pa.Column(
            float, nullable=True, coerce=True
        ),
        "pctinptbedsoccpedperchosprepabschg": pa.Column(
            float, nullable=True, coerce=True
        ),
        "pcticubedsoccadultperchosprepabschg": pa.Column(
            float, nullable=True, coerce=True
        ),
        "pcticubedsoccpedperchosprepabschg": pa.Column(
            float, nullable=True, coerce=True
        ),
        "pctconfc19inptbedsadultperchosprepabschg": pa.Column(
            float, nullable=True, coerce=True
        ),
        "pctconfc19inptbedspedperchosprepabschg": pa.Column(
            float, nullable=True, coerce=True
        ),
        "pctconfc19icubedsadultperchosprepabschg": pa.Column(
            float, nullable=True, coerce=True
        ),
        "pctconfc19icubedspedperchosprepabschg": pa.Column(
            float, nullable=True, coerce=True
        ),
        "pctconffluinptbedsadultperchosprepabschg": pa.Column(
            float, nullable=True, coerce=True
        ),
        "pctconffluinptbedspedperchosprepabschg": pa.Column(
            float, nullable=True, coerce=True
        ),
        "pctconffluicubedsadultperchosprepabschg": pa.Column(
            float, nullable=True, coerce=True
        ),
        "pctconffluicubedspedperchosprepabschg": pa.Column(
            float, nullable=True, coerce=True
        ),
        "pctconfrsvinptbedsadultperchosprepabschg": pa.Column(
            float, nullable=True, coerce=True
        ),
        "pctconfrsvinptbedspedperchosprepabschg": pa.Column(
            float, nullable=True, coerce=True
        ),
        "pctconfrsvicubedsadultperchosprepabschg": pa.Column(
            float, nullable=True, coerce=True
        ),
        "pctconfrsvicubedspedperchosprepabschg": pa.Column(
            float, nullable=True, coerce=True
        ),
        "pctconfc19hosppatsicuperchosprepabschg": pa.Column(
            float, nullable=True, coerce=True
        ),
        "pctconfc19hosppatsicuadultperchosprepabschg": pa.Column(
            float, nullable=True, coerce=True
        ),
        "pctconfc19hosppatsicupedperchosprepabschg": pa.Column(
            float, nullable=True, coerce=True
        ),
        "pctconffluhosppatsicuperchosprepabschg": pa.Column(
            float, nullable=True, coerce=True
        ),
        "pctconffluhosppatsicuadultperchosprepabschg": pa.Column(
            float, nullable=True, coerce=True
        ),
        "pctconffluhosppatsicupedperchosprepabschg": pa.Column(
            float, nullable=True, coerce=True
        ),
        "pctconfrsvhosppatsicuperchosprepabschg": pa.Column(
            float, nullable=True, coerce=True
        ),
        "pctconfrsvhosppatsicuadultperchosprepabschg": pa.Column(
            float, nullable=True, coerce=True
        ),
        "pctconfrsvhosppatsicupedperchosprepabschg": pa.Column(
            float, nullable=True, coerce=True
        ),
        "respseason": pa.Column(str, nullable=True, coerce=True),
        "totalconfc19newadmcumulativeseasonalsum": pa.Column(
            float, nullable=True, coerce=True
        ),
        "totalconfflunewadmcumulativeseasonalsum": pa.Column(
            float, nullable=True, coerce=True
        ),
        "totalconfrsvnewadmcumulativeseasonalsum": pa.Column(
            float, nullable=True, coerce=True
        ),
        "totalconfnewadmcumulativeseasonalsum": pa.Column(
            float, nullable=True, coerce=True
        ),
        "numconfc19icupatsped": pa.Column(float, nullable=True, coerce=True),
        "numconfc19newadmped5to17": pa.Column(
            float, nullable=True, coerce=True
        ),
        "numconfc19newadmped5to17per100k": pa.Column(
            float, nullable=True, coerce=True
        ),
        "pctconfc19icubedsped": pa.Column(float, nullable=True, coerce=True),
        "pctconfc19hosppatsicuped": pa.Column(
            float, nullable=True, coerce=True
        ),
        "numconfc19newadmped0to4": pa.Column(
            float, nullable=True, coerce=True
        ),
        "numconfc19newadmped0to4per100k": pa.Column(
            float, nullable=True, coerce=True
        ),
        "numconfc19newadmped0to4pctchg": pa.Column(
            float, nullable=True, coerce=True
        ),
        "numconfc19newadmped5to17pctchg": pa.Column(
            float, nullable=True, coerce=True
        ),
        "numconffluhosppatsadult": pa.Column(
            float, nullable=True, coerce=True
        ),
        "numconffluhosppatsped": pa.Column(float, nullable=True, coerce=True),
        "numconfrsvhosppatsadult": pa.Column(
            float, nullable=True, coerce=True
        ),
        "numconfrsvhosppatsped": pa.Column(float, nullable=True, coerce=True),
        "totalconfrsvhosppats": pa.Column(float, nullable=True, coerce=True),
        "numconffluicupatsadult": pa.Column(float, nullable=True, coerce=True),
        "numconffluicupatsped": pa.Column(float, nullable=True, coerce=True),
        "numconfrsvicupatsadult": pa.Column(float, nullable=True, coerce=True),
        "numconfrsvicupatsped": pa.Column(float, nullable=True, coerce=True),
        "totalconfrsvicupats": pa.Column(float, nullable=True, coerce=True),
        "numconfc19newadmadult50to64": pa.Column(
            float, nullable=True, coerce=True
        ),
        "numconfc19newadmadult65to74": pa.Column(
            float, nullable=True, coerce=True
        ),
        "numconfc19newadmadult75plus": pa.Column(
            float, nullable=True, coerce=True
        ),
        "numconfflunewadmped0to4": pa.Column(
            float, nullable=True, coerce=True
        ),
        "numconfflunewadmped5to17": pa.Column(
            float, nullable=True, coerce=True
        ),
        "totalconfflunewadmped": pa.Column(float, nullable=True, coerce=True),
        "numconfflunewadmadult18to49": pa.Column(
            float, nullable=True, coerce=True
        ),
        "numconfflunewadmadult50to64": pa.Column(
            float, nullable=True, coerce=True
        ),
        "numconfflunewadmadult65to74": pa.Column(
            float, nullable=True, coerce=True
        ),
        "numconfflunewadmadult75plus": pa.Column(
            float, nullable=True, coerce=True
        ),
        "totalconfflunewadmadult": pa.Column(
            float, nullable=True, coerce=True
        ),
        "numconfflunewadmunk": pa.Column(float, nullable=True, coerce=True),
        "numconfrsvnewadmped0to4": pa.Column(
            float, nullable=True, coerce=True
        ),
        "numconfrsvnewadmped5to17": pa.Column(
            float, nullable=True, coerce=True
        ),
        "totalconfrsvnewadmped": pa.Column(float, nullable=True, coerce=True),
        "numconfrsvnewadmadult18to49": pa.Column(
            float, nullable=True, coerce=True
        ),
        "numconfrsvnewadmadult50to64": pa.Column(
            float, nullable=True, coerce=True
        ),
        "numconfrsvnewadmadult65to74": pa.Column(
            float, nullable=True, coerce=True
        ),
        "numconfrsvnewadmadult75plus": pa.Column(
            float, nullable=True, coerce=True
        ),
        "totalconfrsvnewadmadult": pa.Column(
            float, nullable=True, coerce=True
        ),
        "numconfrsvnewadmunk": pa.Column(float, nullable=True, coerce=True),
        "totalconfrsvnewadm": pa.Column(float, nullable=True, coerce=True),
        "pctconfrsvinptbeds": pa.Column(float, nullable=True, coerce=True),
        "pctconfrsvicubeds": pa.Column(float, nullable=True, coerce=True),
        "pctconfflunewadmadult": pa.Column(float, nullable=True, coerce=True),
        "pctconfflunewadmped": pa.Column(float, nullable=True, coerce=True),
        "pctconfrsvnewadmadult": pa.Column(float, nullable=True, coerce=True),
        "pctconfrsvnewadmped": pa.Column(float, nullable=True, coerce=True),
        "numconfc19newadmadult50to64per100k": pa.Column(
            float, nullable=True, coerce=True
        ),
        "numconfc19newadmadult65to74per100k": pa.Column(
            float, nullable=True, coerce=True
        ),
        "numconfc19newadmadult75plusper100k": pa.Column(
            float, nullable=True, coerce=True
        ),
        "numconfflunewadmped0to4per100k": pa.Column(
            float, nullable=True, coerce=True
        ),
        "numconfflunewadmped5to17per100k": pa.Column(
            float, nullable=True, coerce=True
        ),
        "totalconfflunewadmpedper100k": pa.Column(
            float, nullable=True, coerce=True
        ),
        "numconfflunewadmadult18to49per100k": pa.Column(
            float, nullable=True, coerce=True
        ),
        "numconfflunewadmadult50to64per100k": pa.Column(
            float, nullable=True, coerce=True
        ),
        "numconfflunewadmadult65to74per100k": pa.Column(
            float, nullable=True, coerce=True
        ),
        "numconfflunewadmadult75plusper100k": pa.Column(
            float, nullable=True, coerce=True
        ),
        "totalconfflunewadmadultper100k": pa.Column(
            float, nullable=True, coerce=True
        ),
        "numconfrsvnewadmped0to4per100k": pa.Column(
            float, nullable=True, coerce=True
        ),
        "numconfrsvnewadmped5to17per100k": pa.Column(
            float, nullable=True, coerce=True
        ),
        "totalconfrsvnewadmpedper100k": pa.Column(
            float, nullable=True, coerce=True
        ),
        "numconfrsvnewadmadult18to49per100k": pa.Column(
            float, nullable=True, coerce=True
        ),
        "numconfrsvnewadmadult50to64per100k": pa.Column(
            float, nullable=True, coerce=True
        ),
        "numconfrsvnewadmadult65to74per100k": pa.Column(
            float, nullable=True, coerce=True
        ),
        "numconfrsvnewadmadult75plusper100k": pa.Column(
            float, nullable=True, coerce=True
        ),
        "totalconfrsvnewadmadultper100k": pa.Column(
            float, nullable=True, coerce=True
        ),
        "totalconfrsvnewadmper100k": pa.Column(
            float, nullable=True, coerce=True
        ),
        "pctconffluinptbedsadult": pa.Column(
            float, nullable=True, coerce=True
        ),
        "pctconffluinptbedsped": pa.Column(float, nullable=True, coerce=True),
        "pctconffluicubedsadult": pa.Column(float, nullable=True, coerce=True),
        "pctconffluicubedsped": pa.Column(float, nullable=True, coerce=True),
        "pctconfrsvinptbedsadult": pa.Column(
            float, nullable=True, coerce=True
        ),
        "pctconfrsvinptbedsped": pa.Column(float, nullable=True, coerce=True),
        "pctconfrsvicubedsadult": pa.Column(float, nullable=True, coerce=True),
        "pctconfrsvicubedsped": pa.Column(float, nullable=True, coerce=True),
        "pctconffluhosppatsicuadult": pa.Column(
            float, nullable=True, coerce=True
        ),
        "pctconfrsvhosppatsicu": pa.Column(float, nullable=True, coerce=True),
        "pctconfrsvhosppatsicuadult": pa.Column(
            float, nullable=True, coerce=True
        ),
        "pctconfrsvhosppatsicuped": pa.Column(
            float, nullable=True, coerce=True
        ),
        "numconfc19newadmadult50to64pctchg": pa.Column(
            float, nullable=True, coerce=True
        ),
        "numconfc19newadmadult65to74pctchg": pa.Column(
            float, nullable=True, coerce=True
        ),
        "numconfc19newadmadult75pluspctchg": pa.Column(
            float, nullable=True, coerce=True
        ),
        "numconfflunewadmped5to17pctchg": pa.Column(
            float, nullable=True, coerce=True
        ),
        "totalconfflunewadmpedpctchg": pa.Column(
            float, nullable=True, coerce=True
        ),
        "numconfflunewadmadult18to49pctchg": pa.Column(
            float, nullable=True, coerce=True
        ),
        "numconfflunewadmadult50to64pctchg": pa.Column(
            float, nullable=True, coerce=True
        ),
        "numconfflunewadmadult65to74pctchg": pa.Column(
            float, nullable=True, coerce=True
        ),
        "numconfflunewadmadult75pluspctchg": pa.Column(
            float, nullable=True, coerce=True
        ),
        "totalconfflunewadmadultpctchg": pa.Column(
            float, nullable=True, coerce=True
        ),
        "numconfrsvnewadmped0to4pctchg": pa.Column(
            float, nullable=True, coerce=True
        ),
        "numconfrsvnewadmped5to17pctchg": pa.Column(
            float, nullable=True, coerce=True
        ),
        "totalconfrsvnewadmpedpctchg": pa.Column(
            float, nullable=True, coerce=True
        ),
        "numconfrsvnewadmadult18to49pctchg": pa.Column(
            float, nullable=True, coerce=True
        ),
        "numconfrsvnewadmadult50to64pctchg": pa.Column(
            float, nullable=True, coerce=True
        ),
        "totalconfrsvnewadmadultpctchg": pa.Column(
            float, nullable=True, coerce=True
        ),
        "totalconfrsvnewadmpctchg": pa.Column(
            float, nullable=True, coerce=True
        ),
        "numconfrsvnewadmadult75pluspctchg": pa.Column(
            float, nullable=True, coerce=True
        ),
        "numconfrsvnewadmadult65to74pctchg": pa.Column(
            float, nullable=True, coerce=True
        ),
        "pctconffluhosppatsicuped": pa.Column(
            float, nullable=True, coerce=True
        ),
        "numconfflunewadmped0to4pctchg": pa.Column(
            float, nullable=True, coerce=True
        ),
    }
)


load_schema = pa.DataFrameSchema(
    {
        "weekendingdate": pa.Column(str, nullable=True, coerce=True),
        "jurisdiction": pa.Column(
            str, pa.Check.isin(region_opts), nullable=True, coerce=True
        ),
        "numinptbeds": pa.Column(float, nullable=True, coerce=True),
        "numinptbedsadult": pa.Column(float, nullable=True, coerce=True),
        "numinptbedsped": pa.Column(float, nullable=True, coerce=True),
        "numinptbedsocc": pa.Column(float, nullable=True, coerce=True),
        "numinptbedsoccadult": pa.Column(float, nullable=True, coerce=True),
        "numinptbedsoccped": pa.Column(float, nullable=True, coerce=True),
        "numicubeds": pa.Column(float, nullable=True, coerce=True),
        "numicubedsadult": pa.Column(float, nullable=True, coerce=True),
        "numicubedsped": pa.Column(float, nullable=True, coerce=True),
        "numicubedsocc": pa.Column(float, nullable=True, coerce=True),
        "numicubedsoccadult": pa.Column(float, nullable=True, coerce=True),
        "numicubedsoccped": pa.Column(float, nullable=True, coerce=True),
        "numconfc19hosppatsadult": pa.Column(
            float, nullable=True, coerce=True
        ),
        "numconfc19hosppatsped": pa.Column(float, nullable=True, coerce=True),
        "totalconfc19hosppats": pa.Column(float, nullable=True, coerce=True),
        "totalconffluhosppats": pa.Column(float, nullable=True, coerce=True),
        "numconfc19icupatsadult": pa.Column(float, nullable=True, coerce=True),
        "totalconfc19icupats": pa.Column(float, nullable=True, coerce=True),
        "totalconffluicupats": pa.Column(float, nullable=True, coerce=True),
        "totalconfc19newadmped": pa.Column(float, nullable=True, coerce=True),
        "numconfc19newadmadult18to49": pa.Column(
            float, nullable=True, coerce=True
        ),
        "totalconfc19newadmadult": pa.Column(
            float, nullable=True, coerce=True
        ),
        "numconfc19newadmunk": pa.Column(float, nullable=True, coerce=True),
        "totalconfc19newadm": pa.Column(float, nullable=True, coerce=True),
        "totalconfflunewadm": pa.Column(float, nullable=True, coerce=True),
        "pctinptbedsocc": pa.Column(float, nullable=True, coerce=True),
        "pctconfc19inptbeds": pa.Column(float, nullable=True, coerce=True),
        "pctconffluinptbeds": pa.Column(float, nullable=True, coerce=True),
        "pcticubedsocc": pa.Column(float, nullable=True, coerce=True),
        "pctconfc19icubeds": pa.Column(float, nullable=True, coerce=True),
        "pctconffluicubeds": pa.Column(float, nullable=True, coerce=True),
        "pctconfc19newadmadult": pa.Column(float, nullable=True, coerce=True),
        "pctconfc19newadmped": pa.Column(float, nullable=True, coerce=True),
        "numinptbedshosprep": pa.Column(float, nullable=True, coerce=True),
        "numinptbedsocchosprep": pa.Column(float, nullable=True, coerce=True),
        "numicubedshosprep": pa.Column(float, nullable=True, coerce=True),
        "numicubedsocchosprep": pa.Column(float, nullable=True, coerce=True),
        "totalconfc19hosppatshosprep": pa.Column(
            float, nullable=True, coerce=True
        ),
        "totalconffluhosppatshosprep": pa.Column(
            float, nullable=True, coerce=True
        ),
        "totalconfrsvhosppatshosprep": pa.Column(
            float, nullable=True, coerce=True
        ),
        "totalconfc19icupatshosprep": pa.Column(
            float, nullable=True, coerce=True
        ),
        "totalconffluicupatshosprep": pa.Column(
            float, nullable=True, coerce=True
        ),
        "totalconfrsvicupatshosprep": pa.Column(
            float, nullable=True, coerce=True
        ),
        "totalconfc19newadmpedhosprep": pa.Column(
            float, nullable=True, coerce=True
        ),
        "totalconfc19newadmadulthosprep": pa.Column(
            float, nullable=True, coerce=True
        ),
        "totalconfc19newadmhosprep": pa.Column(
            float, nullable=True, coerce=True
        ),
        "totalconfflunewadmpedhosprep": pa.Column(
            float, nullable=True, coerce=True
        ),
        "totalconfflunewadmadulthosprep": pa.Column(
            float, nullable=True, coerce=True
        ),
        "totalconfflunewadmhosprep": pa.Column(
            float, nullable=True, coerce=True
        ),
        "totalconfrsvnewadmpedhosprep": pa.Column(
            float, nullable=True, coerce=True
        ),
        "totalconfrsvnewadmadulthosprep": pa.Column(
            float, nullable=True, coerce=True
        ),
        "totalconfrsvnewadmhosprep": pa.Column(
            float, nullable=True, coerce=True
        ),
        "pctinptbedsocchosprep": pa.Column(float, nullable=True, coerce=True),
        "pcticubedsocchosprep": pa.Column(float, nullable=True, coerce=True),
        "pctconfc19inptbedshosprep": pa.Column(
            float, nullable=True, coerce=True
        ),
        "pctconffluinptbedshosprep": pa.Column(
            float, nullable=True, coerce=True
        ),
        "pctconfrsvinptbedshosprep": pa.Column(
            float, nullable=True, coerce=True
        ),
        "pctconfc19icubedshosprep": pa.Column(
            float, nullable=True, coerce=True
        ),
        "pctconffluicubedshosprep": pa.Column(
            float, nullable=True, coerce=True
        ),
        "pctconfrsvicubedshosprep": pa.Column(
            float, nullable=True, coerce=True
        ),
        "numinptbedsperchosprep": pa.Column(float, nullable=True, coerce=True),
        "numinptbedsoccperchosprep": pa.Column(
            float, nullable=True, coerce=True
        ),
        "numicubedsperchosprep": pa.Column(float, nullable=True, coerce=True),
        "numicubedsoccperchosprep": pa.Column(
            float, nullable=True, coerce=True
        ),
        "totalconfc19hosppatsperc": pa.Column(
            float, nullable=True, coerce=True
        ),
        "totalconffluhosppatsperc": pa.Column(
            float, nullable=True, coerce=True
        ),
        "totalconfrsvhosppatsperc": pa.Column(
            float, nullable=True, coerce=True
        ),
        "totalconfc19icupatsperchosprep": pa.Column(
            float, nullable=True, coerce=True
        ),
        "totalconffluicupatsperchosprep": pa.Column(
            float, nullable=True, coerce=True
        ),
        "totalconfrsvicupatsperchosprep": pa.Column(
            float, nullable=True, coerce=True
        ),
        "totalconfc19newadmpedper": pa.Column(
            float, nullable=True, coerce=True
        ),
        "totalconfc19newadmadultp": pa.Column(
            float, nullable=True, coerce=True
        ),
        "totalconfc19newadmperchosprep": pa.Column(
            float, nullable=True, coerce=True
        ),
        "totalconfflunewadmpedper": pa.Column(
            float, nullable=True, coerce=True
        ),
        "totalconfflunewadmadultp": pa.Column(
            float, nullable=True, coerce=True
        ),
        "totalconfflunewadmperchosprep": pa.Column(
            float, nullable=True, coerce=True
        ),
        "totalconfrsvnewadmpedper": pa.Column(
            float, nullable=True, coerce=True
        ),
        "totalconfrsvnewadmadultp": pa.Column(
            float, nullable=True, coerce=True
        ),
        "totalconfrsvnewadmperchosprep": pa.Column(
            float, nullable=True, coerce=True
        ),
        "pctinptbedsoccperchosprep": pa.Column(
            float, nullable=True, coerce=True
        ),
        "pcticubedsoccperchosprep": pa.Column(
            float, nullable=True, coerce=True
        ),
        "pctconfc19inptbedsperchosprep": pa.Column(
            float, nullable=True, coerce=True
        ),
        "pctconffluinptbedsperchosprep": pa.Column(
            float, nullable=True, coerce=True
        ),
        "pctconfrsvinptbedsperchosprep": pa.Column(
            float, nullable=True, coerce=True
        ),
        "pctconfc19icubedsperchosprep": pa.Column(
            float, nullable=True, coerce=True
        ),
        "pctconffluicubedsperchosprep": pa.Column(
            float, nullable=True, coerce=True
        ),
        "pctconfrsvicubedsperchosprep": pa.Column(
            float, nullable=True, coerce=True
        ),
        "numinptbedsperchosprepabschg": pa.Column(
            float, nullable=True, coerce=True
        ),
        "numinptbedsoccperchospre": pa.Column(
            float, nullable=True, coerce=True
        ),
        "numicubedsperchosprepabschg": pa.Column(
            float, nullable=True, coerce=True
        ),
        "numicubedsoccperchosprepabschg": pa.Column(
            float, nullable=True, coerce=True
        ),
        "totalconfc19hosppatsperc_1": pa.Column(
            float, nullable=True, coerce=True
        ),
        "totalconffluhosppatsperc_1": pa.Column(
            float, nullable=True, coerce=True
        ),
        "totalconfrsvhosppatsperc_1": pa.Column(
            float, nullable=True, coerce=True
        ),
        "totalconfc19icupatsperch": pa.Column(
            float, nullable=True, coerce=True
        ),
        "totalconffluicupatsperch": pa.Column(
            float, nullable=True, coerce=True
        ),
        "totalconfrsvicupatsperch": pa.Column(
            float, nullable=True, coerce=True
        ),
        "totalconfc19newadmpedper_1": pa.Column(
            float, nullable=True, coerce=True
        ),
        "totalconfc19newadmadultp_1": pa.Column(
            float, nullable=True, coerce=True
        ),
        "totalconfc19newadmpercho": pa.Column(
            float, nullable=True, coerce=True
        ),
        "totalconfflunewadmpedper_1": pa.Column(
            float, nullable=True, coerce=True
        ),
        "totalconfflunewadmadultp_1": pa.Column(
            float, nullable=True, coerce=True
        ),
        "totalconfflunewadmpercho": pa.Column(
            float, nullable=True, coerce=True
        ),
        "totalconfrsvnewadmpedper_1": pa.Column(
            float, nullable=True, coerce=True
        ),
        "totalconfrsvnewadmadultp_1": pa.Column(
            float, nullable=True, coerce=True
        ),
        "totalconfrsvnewadmpercho": pa.Column(
            float, nullable=True, coerce=True
        ),
        "pctinptbedsoccperchospre": pa.Column(
            float, nullable=True, coerce=True
        ),
        "pcticubedsoccperchosprepabschg": pa.Column(
            float, nullable=True, coerce=True
        ),
        "pctconfc19inptbedspercho": pa.Column(
            float, nullable=True, coerce=True
        ),
        "pctconffluinptbedspercho": pa.Column(
            float, nullable=True, coerce=True
        ),
        "pctconfrsvinptbedspercho": pa.Column(
            float, nullable=True, coerce=True
        ),
        "pctconfc19icubedsperchos": pa.Column(
            float, nullable=True, coerce=True
        ),
        "pctconffluicubedsperchos": pa.Column(
            float, nullable=True, coerce=True
        ),
        "pctconfrsvicubedsperchos": pa.Column(
            float, nullable=True, coerce=True
        ),
        "totalconfc19newadmpedper100k": pa.Column(
            float, nullable=True, coerce=True
        ),
        "numconfc19newadmadult18to49per100k": pa.Column(
            float, nullable=True, coerce=True
        ),
        "totalconfc19newadmadultper100k": pa.Column(
            float, nullable=True, coerce=True
        ),
        "totalconfc19newadmper100k": pa.Column(
            float, nullable=True, coerce=True
        ),
        "totalconfflunewadmper100k": pa.Column(
            float, nullable=True, coerce=True
        ),
        "totalconfc19newadmperchosprepabove80pct": pa.Column(
            float, nullable=True, coerce=True
        ),
        "totalconfc19newadmperchosprepabove90pct": pa.Column(
            float, nullable=True, coerce=True
        ),
        "totalconfflunewadmperchosprepabove80pct": pa.Column(
            float, nullable=True, coerce=True
        ),
        "totalconfflunewadmperchosprepabove90pct": pa.Column(
            float, nullable=True, coerce=True
        ),
        "totalconfrsvnewadmperchosprepabove80pct": pa.Column(
            float, nullable=True, coerce=True
        ),
        "totalconfrsvnewadmperchosprepabove90pct": pa.Column(
            float, nullable=True, coerce=True
        ),
        "pctinptbedsoccadult": pa.Column(float, nullable=True, coerce=True),
        "pctinptbedsoccped": pa.Column(float, nullable=True, coerce=True),
        "pcticubedsoccadult": pa.Column(float, nullable=True, coerce=True),
        "pcticubedsoccped": pa.Column(float, nullable=True, coerce=True),
        "pctconfc19inptbedsadult": pa.Column(
            float, nullable=True, coerce=True
        ),
        "pctconfc19inptbedsped": pa.Column(float, nullable=True, coerce=True),
        "pctconfc19icubedsadult": pa.Column(float, nullable=True, coerce=True),
        "pctconfc19hosppatsicu": pa.Column(float, nullable=True, coerce=True),
        "pctconfc19hosppatsicuadult": pa.Column(
            float, nullable=True, coerce=True
        ),
        "pctconffluhosppatsicu": pa.Column(float, nullable=True, coerce=True),
        "totalconfc19newadmpedpctchg": pa.Column(
            float, nullable=True, coerce=True
        ),
        "numconfc19newadmadult18to49pctchg": pa.Column(
            float, nullable=True, coerce=True
        ),
        "totalconfc19newadmadultpctchg": pa.Column(
            float, nullable=True, coerce=True
        ),
        "totalconfc19newadmpctchg": pa.Column(
            float, nullable=True, coerce=True
        ),
        "totalconfflunewadmpctchg": pa.Column(
            float, nullable=True, coerce=True
        ),
        "pctinptbedsoccadulthosprep": pa.Column(
            float, nullable=True, coerce=True
        ),
        "pctinptbedsoccpedhosprep": pa.Column(
            float, nullable=True, coerce=True
        ),
        "pcticubedsoccadulthosprep": pa.Column(
            float, nullable=True, coerce=True
        ),
        "pcticubedsoccpedhosprep": pa.Column(
            float, nullable=True, coerce=True
        ),
        "pctconfc19inptbedsadulthosprep": pa.Column(
            float, nullable=True, coerce=True
        ),
        "pctconfc19inptbedspedhosprep": pa.Column(
            float, nullable=True, coerce=True
        ),
        "pctconfc19icubedsadulthosprep": pa.Column(
            float, nullable=True, coerce=True
        ),
        "pctconfc19icubedspedhosprep": pa.Column(
            float, nullable=True, coerce=True
        ),
        "pctconffluinptbedsadulthosprep": pa.Column(
            float, nullable=True, coerce=True
        ),
        "pctconffluinptbedspedhosprep": pa.Column(
            float, nullable=True, coerce=True
        ),
        "pctconffluicubedsadulthosprep": pa.Column(
            float, nullable=True, coerce=True
        ),
        "pctconffluicubedspedhosprep": pa.Column(
            float, nullable=True, coerce=True
        ),
        "pctconfrsvinptbedsadulthosprep": pa.Column(
            float, nullable=True, coerce=True
        ),
        "pctconfrsvinptbedspedhosprep": pa.Column(
            float, nullable=True, coerce=True
        ),
        "pctconfrsvicubedsadulthosprep": pa.Column(
            float, nullable=True, coerce=True
        ),
        "pctconfrsvicubedspedhosprep": pa.Column(
            float, nullable=True, coerce=True
        ),
        "pctconfc19hosppatsicuhosprep": pa.Column(
            float, nullable=True, coerce=True
        ),
        "pctconfc19hosppatsicuadulthosprep": pa.Column(
            float, nullable=True, coerce=True
        ),
        "pctconfc19hosppatsicupedhosprep": pa.Column(
            float, nullable=True, coerce=True
        ),
        "pctconffluhosppatsicuhosprep": pa.Column(
            float, nullable=True, coerce=True
        ),
        "pctconffluhosppatsicuadulthosprep": pa.Column(
            float, nullable=True, coerce=True
        ),
        "pctconffluhosppatsicupedhosprep": pa.Column(
            float, nullable=True, coerce=True
        ),
        "pctconfrsvhosppatsicuhosprep": pa.Column(
            float, nullable=True, coerce=True
        ),
        "pctconfrsvhosppatsicuadulthosprep": pa.Column(
            float, nullable=True, coerce=True
        ),
        "pctconfrsvhosppatsicupedhosprep": pa.Column(
            float, nullable=True, coerce=True
        ),
        "pctinptbedsoccadultperchosprep": pa.Column(
            float, nullable=True, coerce=True
        ),
        "pctinptbedsoccpedperchosprep": pa.Column(
            float, nullable=True, coerce=True
        ),
        "pcticubedsoccadultperchosprep": pa.Column(
            float, nullable=True, coerce=True
        ),
        "pcticubedsoccpedperchosprep": pa.Column(
            float, nullable=True, coerce=True
        ),
        "pctconfc19inptbedsadultperchosprep": pa.Column(
            float, nullable=True, coerce=True
        ),
        "pctconfc19inptbedspedperchosprep": pa.Column(
            float, nullable=True, coerce=True
        ),
        "pctconfc19icubedsadultperchosprep": pa.Column(
            float, nullable=True, coerce=True
        ),
        "pctconfc19icubedspedperchosprep": pa.Column(
            float, nullable=True, coerce=True
        ),
        "pctconffluinptbedsadultperchosprep": pa.Column(
            float, nullable=True, coerce=True
        ),
        "pctconffluinptbedspedperchosprep": pa.Column(
            float, nullable=True, coerce=True
        ),
        "pctconffluicubedsadultperchosprep": pa.Column(
            float, nullable=True, coerce=True
        ),
        "pctconffluicubedspedperchosprep": pa.Column(
            float, nullable=True, coerce=True
        ),
        "pctconfrsvinptbedsadultperchosprep": pa.Column(
            float, nullable=True, coerce=True
        ),
        "pctconfrsvinptbedspedperchosprep": pa.Column(
            float, nullable=True, coerce=True
        ),
        "pctconfrsvicubedsadultperchosprep": pa.Column(
            float, nullable=True, coerce=True
        ),
        "pctconfrsvicubedspedperchosprep": pa.Column(
            float, nullable=True, coerce=True
        ),
        "pctconfc19hosppatsicuperchosprep": pa.Column(
            float, nullable=True, coerce=True
        ),
        "pctconfc19hosppatsicuadultperchosprep": pa.Column(
            float, nullable=True, coerce=True
        ),
        "pctconfc19hosppatsicupedperchosprep": pa.Column(
            float, nullable=True, coerce=True
        ),
        "pctconffluhosppatsicuperchosprep": pa.Column(
            float, nullable=True, coerce=True
        ),
        "pctconffluhosppatsicuadultperchosprep": pa.Column(
            float, nullable=True, coerce=True
        ),
        "pctconffluhosppatsicupedperchosprep": pa.Column(
            float, nullable=True, coerce=True
        ),
        "pctconfrsvhosppatsicuperchosprep": pa.Column(
            float, nullable=True, coerce=True
        ),
        "pctconfrsvhosppatsicuadultperchosprep": pa.Column(
            float, nullable=True, coerce=True
        ),
        "pctconfrsvhosppatsicupedperchosprep": pa.Column(
            float, nullable=True, coerce=True
        ),
        "pctinptbedsoccadultperchosprepabschg": pa.Column(
            float, nullable=True, coerce=True
        ),
        "pctinptbedsoccpedperchosprepabschg": pa.Column(
            float, nullable=True, coerce=True
        ),
        "pcticubedsoccadultperchosprepabschg": pa.Column(
            float, nullable=True, coerce=True
        ),
        "pcticubedsoccpedperchosprepabschg": pa.Column(
            float, nullable=True, coerce=True
        ),
        "pctconfc19inptbedsadultperchosprepabschg": pa.Column(
            float, nullable=True, coerce=True
        ),
        "pctconfc19inptbedspedperchosprepabschg": pa.Column(
            float, nullable=True, coerce=True
        ),
        "pctconfc19icubedsadultperchosprepabschg": pa.Column(
            float, nullable=True, coerce=True
        ),
        "pctconfc19icubedspedperchosprepabschg": pa.Column(
            float, nullable=True, coerce=True
        ),
        "pctconffluinptbedsadultperchosprepabschg": pa.Column(
            float, nullable=True, coerce=True
        ),
        "pctconffluinptbedspedperchosprepabschg": pa.Column(
            float, nullable=True, coerce=True
        ),
        "pctconffluicubedsadultperchosprepabschg": pa.Column(
            float, nullable=True, coerce=True
        ),
        "pctconffluicubedspedperchosprepabschg": pa.Column(
            float, nullable=True, coerce=True
        ),
        "pctconfrsvinptbedsadultperchosprepabschg": pa.Column(
            float, nullable=True, coerce=True
        ),
        "pctconfrsvinptbedspedperchosprepabschg": pa.Column(
            float, nullable=True, coerce=True
        ),
        "pctconfrsvicubedsadultperchosprepabschg": pa.Column(
            float, nullable=True, coerce=True
        ),
        "pctconfrsvicubedspedperchosprepabschg": pa.Column(
            float, nullable=True, coerce=True
        ),
        "pctconfc19hosppatsicuperchosprepabschg": pa.Column(
            float, nullable=True, coerce=True
        ),
        "pctconfc19hosppatsicuadultperchosprepabschg": pa.Column(
            float, nullable=True, coerce=True
        ),
        "pctconfc19hosppatsicupedperchosprepabschg": pa.Column(
            float, nullable=True, coerce=True
        ),
        "pctconffluhosppatsicuperchosprepabschg": pa.Column(
            float, nullable=True, coerce=True
        ),
        "pctconffluhosppatsicuadultperchosprepabschg": pa.Column(
            float, nullable=True, coerce=True
        ),
        "pctconffluhosppatsicupedperchosprepabschg": pa.Column(
            float, nullable=True, coerce=True
        ),
        "pctconfrsvhosppatsicuperchosprepabschg": pa.Column(
            float, nullable=True, coerce=True
        ),
        "pctconfrsvhosppatsicuadultperchosprepabschg": pa.Column(
            float, nullable=True, coerce=True
        ),
        "pctconfrsvhosppatsicupedperchosprepabschg": pa.Column(
            float, nullable=True, coerce=True
        ),
        "respseason": pa.Column(str, nullable=True, coerce=True),
        "totalconfc19newadmcumulativeseasonalsum": pa.Column(
            float, nullable=True, coerce=True
        ),
        "totalconfflunewadmcumulativeseasonalsum": pa.Column(
            float, nullable=True, coerce=True
        ),
        "totalconfrsvnewadmcumulativeseasonalsum": pa.Column(
            float, nullable=True, coerce=True
        ),
        "totalconfnewadmcumulativeseasonalsum": pa.Column(
            float, nullable=True, coerce=True
        ),
        "numconfc19icupatsped": pa.Column(float, nullable=True, coerce=True),
        "numconfc19newadmped5to17": pa.Column(
            float, nullable=True, coerce=True
        ),
        "numconfc19newadmped5to17per100k": pa.Column(
            float, nullable=True, coerce=True
        ),
        "pctconfc19icubedsped": pa.Column(float, nullable=True, coerce=True),
        "pctconfc19hosppatsicuped": pa.Column(
            float, nullable=True, coerce=True
        ),
        "numconfc19newadmped0to4": pa.Column(
            float, nullable=True, coerce=True
        ),
        "numconfc19newadmped0to4per100k": pa.Column(
            float, nullable=True, coerce=True
        ),
        "numconfc19newadmped0to4pctchg": pa.Column(
            float, nullable=True, coerce=True
        ),
        "numconfc19newadmped5to17pctchg": pa.Column(
            float, nullable=True, coerce=True
        ),
        "numconffluhosppatsadult": pa.Column(
            float, nullable=True, coerce=True
        ),
        "numconffluhosppatsped": pa.Column(float, nullable=True, coerce=True),
        "numconfrsvhosppatsadult": pa.Column(
            float, nullable=True, coerce=True
        ),
        "numconfrsvhosppatsped": pa.Column(float, nullable=True, coerce=True),
        "totalconfrsvhosppats": pa.Column(float, nullable=True, coerce=True),
        "numconffluicupatsadult": pa.Column(float, nullable=True, coerce=True),
        "numconffluicupatsped": pa.Column(float, nullable=True, coerce=True),
        "numconfrsvicupatsadult": pa.Column(float, nullable=True, coerce=True),
        "numconfrsvicupatsped": pa.Column(float, nullable=True, coerce=True),
        "totalconfrsvicupats": pa.Column(float, nullable=True, coerce=True),
        "numconfc19newadmadult50to64": pa.Column(
            float, nullable=True, coerce=True
        ),
        "numconfc19newadmadult65to74": pa.Column(
            float, nullable=True, coerce=True
        ),
        "numconfc19newadmadult75plus": pa.Column(
            float, nullable=True, coerce=True
        ),
        "numconfflunewadmped0to4": pa.Column(
            float, nullable=True, coerce=True
        ),
        "numconfflunewadmped5to17": pa.Column(
            float, nullable=True, coerce=True
        ),
        "totalconfflunewadmped": pa.Column(float, nullable=True, coerce=True),
        "numconfflunewadmadult18to49": pa.Column(
            float, nullable=True, coerce=True
        ),
        "numconfflunewadmadult50to64": pa.Column(
            float, nullable=True, coerce=True
        ),
        "numconfflunewadmadult65to74": pa.Column(
            float, nullable=True, coerce=True
        ),
        "numconfflunewadmadult75plus": pa.Column(
            float, nullable=True, coerce=True
        ),
        "totalconfflunewadmadult": pa.Column(
            float, nullable=True, coerce=True
        ),
        "numconfflunewadmunk": pa.Column(float, nullable=True, coerce=True),
        "numconfrsvnewadmped0to4": pa.Column(
            float, nullable=True, coerce=True
        ),
        "numconfrsvnewadmped5to17": pa.Column(
            float, nullable=True, coerce=True
        ),
        "totalconfrsvnewadmped": pa.Column(float, nullable=True, coerce=True),
        "numconfrsvnewadmadult18to49": pa.Column(
            float, nullable=True, coerce=True
        ),
        "numconfrsvnewadmadult50to64": pa.Column(
            float, nullable=True, coerce=True
        ),
        "numconfrsvnewadmadult65to74": pa.Column(
            float, nullable=True, coerce=True
        ),
        "numconfrsvnewadmadult75plus": pa.Column(
            float, nullable=True, coerce=True
        ),
        "totalconfrsvnewadmadult": pa.Column(
            float, nullable=True, coerce=True
        ),
        "numconfrsvnewadmunk": pa.Column(float, nullable=True, coerce=True),
        "totalconfrsvnewadm": pa.Column(float, nullable=True, coerce=True),
        "pctconfrsvinptbeds": pa.Column(float, nullable=True, coerce=True),
        "pctconfrsvicubeds": pa.Column(float, nullable=True, coerce=True),
        "pctconfflunewadmadult": pa.Column(float, nullable=True, coerce=True),
        "pctconfflunewadmped": pa.Column(float, nullable=True, coerce=True),
        "pctconfrsvnewadmadult": pa.Column(float, nullable=True, coerce=True),
        "pctconfrsvnewadmped": pa.Column(float, nullable=True, coerce=True),
        "numconfc19newadmadult50to64per100k": pa.Column(
            float, nullable=True, coerce=True
        ),
        "numconfc19newadmadult65to74per100k": pa.Column(
            float, nullable=True, coerce=True
        ),
        "numconfc19newadmadult75plusper100k": pa.Column(
            float, nullable=True, coerce=True
        ),
        "numconfflunewadmped0to4per100k": pa.Column(
            float, nullable=True, coerce=True
        ),
        "numconfflunewadmped5to17per100k": pa.Column(
            float, nullable=True, coerce=True
        ),
        "totalconfflunewadmpedper100k": pa.Column(
            float, nullable=True, coerce=True
        ),
        "numconfflunewadmadult18to49per100k": pa.Column(
            float, nullable=True, coerce=True
        ),
        "numconfflunewadmadult50to64per100k": pa.Column(
            float, nullable=True, coerce=True
        ),
        "numconfflunewadmadult65to74per100k": pa.Column(
            float, nullable=True, coerce=True
        ),
        "numconfflunewadmadult75plusper100k": pa.Column(
            float, nullable=True, coerce=True
        ),
        "totalconfflunewadmadultper100k": pa.Column(
            float, nullable=True, coerce=True
        ),
        "numconfrsvnewadmped0to4per100k": pa.Column(
            float, nullable=True, coerce=True
        ),
        "numconfrsvnewadmped5to17per100k": pa.Column(
            float, nullable=True, coerce=True
        ),
        "totalconfrsvnewadmpedper100k": pa.Column(
            float, nullable=True, coerce=True
        ),
        "numconfrsvnewadmadult18to49per100k": pa.Column(
            float, nullable=True, coerce=True
        ),
        "numconfrsvnewadmadult50to64per100k": pa.Column(
            float, nullable=True, coerce=True
        ),
        "numconfrsvnewadmadult65to74per100k": pa.Column(
            float, nullable=True, coerce=True
        ),
        "numconfrsvnewadmadult75plusper100k": pa.Column(
            float, nullable=True, coerce=True
        ),
        "totalconfrsvnewadmadultper100k": pa.Column(
            float, nullable=True, coerce=True
        ),
        "totalconfrsvnewadmper100k": pa.Column(
            float, nullable=True, coerce=True
        ),
        "pctconffluinptbedsadult": pa.Column(
            float, nullable=True, coerce=True
        ),
        "pctconffluinptbedsped": pa.Column(float, nullable=True, coerce=True),
        "pctconffluicubedsadult": pa.Column(float, nullable=True, coerce=True),
        "pctconffluicubedsped": pa.Column(float, nullable=True, coerce=True),
        "pctconfrsvinptbedsadult": pa.Column(
            float, nullable=True, coerce=True
        ),
        "pctconfrsvinptbedsped": pa.Column(float, nullable=True, coerce=True),
        "pctconfrsvicubedsadult": pa.Column(float, nullable=True, coerce=True),
        "pctconfrsvicubedsped": pa.Column(float, nullable=True, coerce=True),
        "pctconffluhosppatsicuadult": pa.Column(
            float, nullable=True, coerce=True
        ),
        "pctconfrsvhosppatsicu": pa.Column(float, nullable=True, coerce=True),
        "pctconfrsvhosppatsicuadult": pa.Column(
            float, nullable=True, coerce=True
        ),
        "pctconfrsvhosppatsicuped": pa.Column(
            float, nullable=True, coerce=True
        ),
        "numconfc19newadmadult50to64pctchg": pa.Column(
            float, nullable=True, coerce=True
        ),
        "numconfc19newadmadult65to74pctchg": pa.Column(
            float, nullable=True, coerce=True
        ),
        "numconfc19newadmadult75pluspctchg": pa.Column(
            float, nullable=True, coerce=True
        ),
        "numconfflunewadmped5to17pctchg": pa.Column(
            float, nullable=True, coerce=True
        ),
        "totalconfflunewadmpedpctchg": pa.Column(
            float, nullable=True, coerce=True
        ),
        "numconfflunewadmadult18to49pctchg": pa.Column(
            float, nullable=True, coerce=True
        ),
        "numconfflunewadmadult50to64pctchg": pa.Column(
            float, nullable=True, coerce=True
        ),
        "numconfflunewadmadult65to74pctchg": pa.Column(
            float, nullable=True, coerce=True
        ),
        "numconfflunewadmadult75pluspctchg": pa.Column(
            float, nullable=True, coerce=True
        ),
        "totalconfflunewadmadultpctchg": pa.Column(
            float, nullable=True, coerce=True
        ),
        "numconfrsvnewadmped0to4pctchg": pa.Column(
            float, nullable=True, coerce=True
        ),
        "numconfrsvnewadmped5to17pctchg": pa.Column(
            float, nullable=True, coerce=True
        ),
        "totalconfrsvnewadmpedpctchg": pa.Column(
            float, nullable=True, coerce=True
        ),
        "numconfrsvnewadmadult18to49pctchg": pa.Column(
            float, nullable=True, coerce=True
        ),
        "numconfrsvnewadmadult50to64pctchg": pa.Column(
            float, nullable=True, coerce=True
        ),
        "totalconfrsvnewadmadultpctchg": pa.Column(
            float, nullable=True, coerce=True
        ),
        "totalconfrsvnewadmpctchg": pa.Column(
            float, nullable=True, coerce=True
        ),
        "numconfrsvnewadmadult75pluspctchg": pa.Column(
            float, nullable=True, coerce=True
        ),
        "numconfrsvnewadmadult65to74pctchg": pa.Column(
            float, nullable=True, coerce=True
        ),
        "pctconffluhosppatsicuped": pa.Column(
            float, nullable=True, coerce=True
        ),
        "numconfflunewadmped0to4pctchg": pa.Column(
            float, nullable=True, coerce=True
        ),
    }
)


def extract_mock_data(output="pandas", size=10) -> pd.DataFrame | pl.DataFrame:
    data = {
        "weekendingdate": [fake.date() for _ in range(size)],
        "jurisdiction": [random.choice(region_opts) for _ in range(size)],
        "numinptbeds": [random.uniform(7, 831870) for _ in range(size)],
        "numinptbedsadult": [random.uniform(3, 743870) for _ in range(size)],
        "numinptbedsped": [random.uniform(0, 84581) for _ in range(size)],
        "numinptbedsocc": [random.uniform(0, 587461) for _ in range(size)],
        "numinptbedsoccadult": [
            random.uniform(0, 543870) for _ in range(size)
        ],
        "numinptbedsoccped": [random.uniform(0, 84581) for _ in range(size)],
        "numicubeds": [random.uniform(0, 100000) for _ in range(size)],
        "numicubedsadult": [random.uniform(0, 90000) for _ in range(size)],
        "numicubedsped": [random.uniform(0, 10000) for _ in range(size)],
        "numicubedsocc": [random.uniform(0, 90000) for _ in range(size)],
        "numicubedsoccadult": [random.uniform(0, 80000) for _ in range(size)],
        "numicubedsoccped": [random.uniform(0, 10000) for _ in range(size)],
        "numconfc19hosppatsadult": [
            random.uniform(0, 50000) for _ in range(size)
        ],
        "numconfc19hosppatsped": [
            random.uniform(0, 10000) for _ in range(size)
        ],
        "totalconfc19hosppats": [
            random.uniform(0, 60000) for _ in range(size)
        ],
        "totalconffluhosppats": [
            random.uniform(0, 50000) for _ in range(size)
        ],
        "numconfc19icupatsadult": [
            random.uniform(0, 10000) for _ in range(size)
        ],
        "totalconfc19icupats": [random.uniform(0, 15000) for _ in range(size)],
        "totalconffluicupats": [random.uniform(0, 12000) for _ in range(size)],
        "totalconfc19newadmped": [
            random.uniform(0, 10000) for _ in range(size)
        ],
        "numconfc19newadmadult18to49": [
            random.uniform(0, 20000) for _ in range(size)
        ],
        "totalconfc19newadmadult": [
            random.uniform(0, 30000) for _ in range(size)
        ],
        "numconfc19newadmunk": [random.uniform(0, 5000) for _ in range(size)],
        "totalconfc19newadm": [random.uniform(0, 40000) for _ in range(size)],
        "totalconfflunewadm": [random.uniform(0, 35000) for _ in range(size)],
        "pctinptbedsocc": [random.uniform(0, 100) for _ in range(size)],
        "pctconfc19inptbeds": [random.uniform(0, 100) for _ in range(size)],
        "pctconffluinptbeds": [random.uniform(0, 100) for _ in range(size)],
        "pcticubedsocc": [random.uniform(0, 100) for _ in range(size)],
        "pctconfc19icubeds": [random.uniform(0, 100) for _ in range(size)],
        "pctconffluicubeds": [random.uniform(0, 100) for _ in range(size)],
        "pctconfc19newadmadult": [random.uniform(0, 100) for _ in range(size)],
        "pctconfc19newadmped": [random.uniform(0, 100) for _ in range(size)],
        "numinptbedshosprep": [random.uniform(0, 500000) for _ in range(size)],
        "numinptbedsocchosprep": [
            random.uniform(0, 400000) for _ in range(size)
        ],
        "numicubedshosprep": [random.uniform(0, 100000) for _ in range(size)],
        "numicubedsocchosprep": [
            random.uniform(0, 90000) for _ in range(size)
        ],
        "totalconfc19hosppatshosprep": [
            random.uniform(0, 60000) for _ in range(size)
        ],
        "totalconffluhosppatshosprep": [
            random.uniform(0, 50000) for _ in range(size)
        ],
        "totalconfrsvhosppatshosprep": [
            random.uniform(0, 40000) for _ in range(size)
        ],
        "totalconfc19icupatshosprep": [
            random.uniform(0, 15000) for _ in range(size)
        ],
        "totalconffluicupatshosprep": [
            random.uniform(0, 12000) for _ in range(size)
        ],
        "totalconfrsvicupatshosprep": [
            random.uniform(0, 10000) for _ in range(size)
        ],
        "totalconfc19newadmpedhosprep": [
            random.uniform(0, 10000) for _ in range(size)
        ],
        "totalconfc19newadmadulthosprep": [
            random.uniform(0, 30000) for _ in range(size)
        ],
        "totalconfc19newadmhosprep": [
            random.uniform(0, 40000) for _ in range(size)
        ],
        "totalconfflunewadmpedhosprep": [
            random.uniform(0, 35000) for _ in range(size)
        ],
        "totalconfflunewadmadulthosprep": [
            random.uniform(0, 35000) for _ in range(size)
        ],
        "totalconfflunewadmhosprep": [
            random.uniform(0, 40000) for _ in range(size)
        ],
        "totalconfrsvnewadmpedhosprep": [
            random.uniform(0, 30000) for _ in range(size)
        ],
        "totalconfrsvnewadmadulthosprep": [
            random.uniform(0, 30000) for _ in range(size)
        ],
        "totalconfrsvnewadmhosprep": [
            random.uniform(0, 35000) for _ in range(size)
        ],
        "pctinptbedsocchosprep": [random.uniform(0, 100) for _ in range(size)],
        "pcticubedsocchosprep": [random.uniform(0, 100) for _ in range(size)],
        "pctconfc19inptbedshosprep": [
            random.uniform(0, 100) for _ in range(size)
        ],
        "pctconffluinptbedshosprep": [
            random.uniform(0, 100) for _ in range(size)
        ],
        "pctconfrsvinptbedshosprep": [
            random.uniform(0, 100) for _ in range(size)
        ],
        "pctconfc19icubedshosprep": [
            random.uniform(0, 100) for _ in range(size)
        ],
        "pctconffluicubedshosprep": [
            random.uniform(0, 100) for _ in range(size)
        ],
        "pctconfrsvicubedshosprep": [
            random.uniform(0, 100) for _ in range(size)
        ],
        "numinptbedsperchosprep": [
            random.uniform(0, 1000) for _ in range(size)
        ],
        "numinptbedsoccperchosprep": [
            random.uniform(0, 1000) for _ in range(size)
        ],
        "numicubedsperchosprep": [random.uniform(0, 500) for _ in range(size)],
        "numicubedsoccperchosprep": [
            random.uniform(0, 500) for _ in range(size)
        ],
        "totalconfc19hosppatsperc": [
            random.uniform(0, 100) for _ in range(size)
        ],
        "totalconffluhosppatsperc": [
            random.uniform(0, 100) for _ in range(size)
        ],
        "totalconfrsvhosppatsperc": [
            random.uniform(0, 100) for _ in range(size)
        ],
        "totalconfc19icupatsperchosprep": [
            random.uniform(0, 100) for _ in range(size)
        ],
        "totalconffluicupatsperchosprep": [
            random.uniform(0, 100) for _ in range(size)
        ],
        "totalconfrsvicupatsperchosprep": [
            random.uniform(0, 100) for _ in range(size)
        ],
        "totalconfc19newadmpedper": [
            random.uniform(0, 100) for _ in range(size)
        ],
        "totalconfc19newadmadultp": [
            random.uniform(0, 100) for _ in range(size)
        ],
        "totalconfc19newadmperchosprep": [
            random.uniform(0, 100) for _ in range(size)
        ],
        "totalconfflunewadmpedper": [
            random.uniform(0, 100) for _ in range(size)
        ],
        "totalconfflunewadmadultp": [
            random.uniform(0, 100) for _ in range(size)
        ],
        "totalconfflunewadmperchosprep": [
            random.uniform(0, 100) for _ in range(size)
        ],
        "totalconfrsvnewadmpedper": [
            random.uniform(0, 100) for _ in range(size)
        ],
        "totalconfrsvnewadmadultp": [
            random.uniform(0, 100) for _ in range(size)
        ],
        "totalconfrsvnewadmperchosprep": [
            random.uniform(0, 100) for _ in range(size)
        ],
        "pctinptbedsoccperchosprep": [
            random.uniform(0, 100) for _ in range(size)
        ],
        "pcticubedsoccperchosprep": [
            random.uniform(0, 100) for _ in range(size)
        ],
        "pctconfc19inptbedsperchosprep": [
            random.uniform(0, 100) for _ in range(size)
        ],
        "pctconffluinptbedsperchosprep": [
            random.uniform(0, 100) for _ in range(size)
        ],
        "pctconfrsvinptbedsperchosprep": [
            random.uniform(0, 100) for _ in range(size)
        ],
        "pctconfc19icubedsperchosprep": [
            random.uniform(0, 100) for _ in range(size)
        ],
        "pctconffluicubedsperchosprep": [
            random.uniform(0, 100) for _ in range(size)
        ],
        "pctconfrsvicubedsperchosprep": [
            random.uniform(0, 100) for _ in range(size)
        ],
        "numinptbedsperchosprepabschg": [
            random.uniform(0, 1000) for _ in range(size)
        ],
        "numinptbedsoccperchospre": [
            random.uniform(0, 1000) for _ in range(size)
        ],
        "numicubedsperchosprepabschg": [
            random.uniform(0, 500) for _ in range(size)
        ],
        "numicubedsoccperchosprepabschg": [
            random.uniform(0, 500) for _ in range(size)
        ],
        "totalconfc19hosppatsperc_1": [
            random.uniform(0, 100) for _ in range(size)
        ],
        "totalconffluhosppatsperc_1": [
            random.uniform(0, 100) for _ in range(size)
        ],
        "totalconfrsvhosppatsperc_1": [
            random.uniform(0, 100) for _ in range(size)
        ],
        "totalconfc19icupatsperch": [
            random.uniform(0, 100) for _ in range(size)
        ],
        "totalconffluicupatsperch": [
            random.uniform(0, 100) for _ in range(size)
        ],
        "totalconfrsvicupatsperch": [
            random.uniform(0, 100) for _ in range(size)
        ],
        "totalconfc19newadmpedper_1": [
            random.uniform(0, 100) for _ in range(size)
        ],
        "totalconfc19newadmadultp_1": [
            random.uniform(0, 100) for _ in range(size)
        ],
        "totalconfc19newadmpercho": [
            random.uniform(0, 100) for _ in range(size)
        ],
        "totalconfflunewadmpedper_1": [
            random.uniform(0, 100) for _ in range(size)
        ],
        "totalconfflunewadmadultp_1": [
            random.uniform(0, 100) for _ in range(size)
        ],
        "totalconfflunewadmpercho": [
            random.uniform(0, 100) for _ in range(size)
        ],
        "totalconfrsvnewadmpedper_1": [
            random.uniform(0, 100) for _ in range(size)
        ],
        "totalconfrsvnewadmadultp_1": [
            random.uniform(0, 100) for _ in range(size)
        ],
        "totalconfrsvnewadmpercho": [
            random.uniform(0, 100) for _ in range(size)
        ],
        "pctinptbedsoccperchospre": [
            random.uniform(0, 100) for _ in range(size)
        ],
        "pcticubedsoccperchosprepabschg": [
            random.uniform(0, 100) for _ in range(size)
        ],
        "pctconfc19inptbedspercho": [
            random.uniform(0, 100) for _ in range(size)
        ],
        "pctconffluinptbedspercho": [
            random.uniform(0, 100) for _ in range(size)
        ],
        "pctconfrsvinptbedspercho": [
            random.uniform(0, 100) for _ in range(size)
        ],
        "pctconfc19icubedsperchos": [
            random.uniform(0, 100) for _ in range(size)
        ],
        "pctconffluicubedsperchos": [
            random.uniform(0, 100) for _ in range(size)
        ],
        "pctconfrsvicubedsperchos": [
            random.uniform(0, 100) for _ in range(size)
        ],
        "totalconfc19newadmpedper100k": [
            random.uniform(0, 100) for _ in range(size)
        ],
        "numconfc19newadmadult18to49per100k": [
            random.uniform(0, 100) for _ in range(size)
        ],
        "totalconfc19newadmadultper100k": [
            random.uniform(0, 100) for _ in range(size)
        ],
        "totalconfc19newadmper100k": [
            random.uniform(0, 100) for _ in range(size)
        ],
        "totalconfflunewadmper100k": [
            random.uniform(0, 100) for _ in range(size)
        ],
        "totalconfc19newadmperchosprepabove80pct": [
            random.uniform(0, 100) for _ in range(size)
        ],
        "totalconfc19newadmperchosprepabove90pct": [
            random.uniform(0, 100) for _ in range(size)
        ],
        "totalconfflunewadmperchosprepabove80pct": [
            random.uniform(0, 100) for _ in range(size)
        ],
        "totalconfflunewadmperchosprepabove90pct": [
            random.uniform(0, 100) for _ in range(size)
        ],
        "totalconfrsvnewadmperchosprepabove80pct": [
            random.uniform(0, 100) for _ in range(size)
        ],
        "totalconfrsvnewadmperchosprepabove90pct": [
            random.uniform(0, 100) for _ in range(size)
        ],
        "pctinptbedsoccadult": [random.uniform(0, 100) for _ in range(size)],
        "pctinptbedsoccped": [random.uniform(0, 100) for _ in range(size)],
        "pcticubedsoccadult": [random.uniform(0, 100) for _ in range(size)],
        "pcticubedsoccped": [random.uniform(0, 100) for _ in range(size)],
        "pctconfc19inptbedsadult": [
            random.uniform(0, 100) for _ in range(size)
        ],
        "pctconfc19inptbedsped": [random.uniform(0, 100) for _ in range(size)],
        "pctconfc19icubedsadult": [
            random.uniform(0, 100) for _ in range(size)
        ],
        "pctconfc19hosppatsicu": [random.uniform(0, 100) for _ in range(size)],
        "pctconfc19hosppatsicuadult": [
            random.uniform(0, 100) for _ in range(size)
        ],
        "pctconffluhosppatsicu": [random.uniform(0, 100) for _ in range(size)],
        "totalconfc19newadmpedpctchg": [
            random.uniform(-100, 100) for _ in range(size)
        ],
        "numconfc19newadmadult18to49pctchg": [
            random.uniform(-100, 100) for _ in range(size)
        ],
        "totalconfc19newadmadultpctchg": [
            random.uniform(-100, 100) for _ in range(size)
        ],
        "totalconfc19newadmpctchg": [
            random.uniform(-100, 100) for _ in range(size)
        ],
        "totalconfflunewadmpctchg": [
            random.uniform(-100, 100) for _ in range(size)
        ],
        "pctinptbedsoccadulthosprep": [
            random.uniform(0, 100) for _ in range(size)
        ],
        "pctinptbedsoccpedhosprep": [
            random.uniform(0, 100) for _ in range(size)
        ],
        "pcticubedsoccadulthosprep": [
            random.uniform(0, 100) for _ in range(size)
        ],
        "pcticubedsoccpedhosprep": [
            random.uniform(0, 100) for _ in range(size)
        ],
        "pctconfc19inptbedsadulthosprep": [
            random.uniform(0, 100) for _ in range(size)
        ],
        "pctconfc19inptbedspedhosprep": [
            random.uniform(0, 100) for _ in range(size)
        ],
        "pctconfc19icubedsadulthosprep": [
            random.uniform(0, 100) for _ in range(size)
        ],
        "pctconfc19icubedspedhosprep": [
            random.uniform(0, 100) for _ in range(size)
        ],
        "pctconffluinptbedsadulthosprep": [
            random.uniform(0, 100) for _ in range(size)
        ],
        "pctconffluinptbedspedhosprep": [
            random.uniform(0, 100) for _ in range(size)
        ],
        "pctconffluicubedsadulthosprep": [
            random.uniform(0, 100) for _ in range(size)
        ],
        "pctconffluicubedspedhosprep": [
            random.uniform(0, 100) for _ in range(size)
        ],
        "pctconfrsvinptbedsadulthosprep": [
            random.uniform(0, 100) for _ in range(size)
        ],
        "pctconfrsvinptbedspedhosprep": [
            random.uniform(0, 100) for _ in range(size)
        ],
        "pctconfrsvicubedsadulthosprep": [
            random.uniform(0, 100) for _ in range(size)
        ],
        "pctconfrsvicubedspedhosprep": [
            random.uniform(0, 100) for _ in range(size)
        ],
        "pctconfc19hosppatsicuhosprep": [
            random.uniform(0, 100) for _ in range(size)
        ],
        "pctconfc19hosppatsicuadulthosprep": [
            random.uniform(0, 100) for _ in range(size)
        ],
        "pctconfc19hosppatsicupedhosprep": [
            random.uniform(0, 100) for _ in range(size)
        ],
        "pctconffluhosppatsicuhosprep": [
            random.uniform(0, 100) for _ in range(size)
        ],
        "pctconffluhosppatsicuadulthosprep": [
            random.uniform(0, 100) for _ in range(size)
        ],
        "pctconffluhosppatsicupedhosprep": [
            random.uniform(0, 100) for _ in range(size)
        ],
        "pctconfrsvhosppatsicuhosprep": [
            random.uniform(0, 100) for _ in range(size)
        ],
        "pctconfrsvhosppatsicuadulthosprep": [
            random.uniform(0, 100) for _ in range(size)
        ],
        "pctconfrsvhosppatsicupedhosprep": [
            random.uniform(0, 100) for _ in range(size)
        ],
        "pctinptbedsoccadultperchosprep": [
            random.uniform(0, 100) for _ in range(size)
        ],
        "pctinptbedsoccpedperchosprep": [
            random.uniform(0, 100) for _ in range(size)
        ],
        "pcticubedsoccadultperchosprep": [
            random.uniform(0, 100) for _ in range(size)
        ],
        "pcticubedsoccpedperchosprep": [
            random.uniform(0, 100) for _ in range(size)
        ],
        "pctconfc19inptbedsadultperchosprep": [
            random.uniform(0, 100) for _ in range(size)
        ],
        "pctconfc19inptbedspedperchosprep": [
            random.uniform(0, 100) for _ in range(size)
        ],
        "pctconfc19icubedsadultperchosprep": [
            random.uniform(0, 100) for _ in range(size)
        ],
        "pctconfc19icubedspedperchosprep": [
            random.uniform(0, 100) for _ in range(size)
        ],
        "pctconffluinptbedsadultperchosprep": [
            random.uniform(0, 100) for _ in range(size)
        ],
        "pctconffluinptbedspedperchosprep": [
            random.uniform(0, 100) for _ in range(size)
        ],
        "pctconffluicubedsadultperchosprep": [
            random.uniform(0, 100) for _ in range(size)
        ],
        "pctconffluicubedspedperchosprep": [
            random.uniform(0, 100) for _ in range(size)
        ],
        "pctconfrsvinptbedsadultperchosprep": [
            random.uniform(0, 100) for _ in range(size)
        ],
        "pctconfrsvinptbedspedperchosprep": [
            random.uniform(0, 100) for _ in range(size)
        ],
        "pctconfrsvicubedsadultperchosprep": [
            random.uniform(0, 100) for _ in range(size)
        ],
        "pctconfrsvicubedspedperchosprep": [
            random.uniform(0, 100) for _ in range(size)
        ],
        "pctconfc19hosppatsicuperchosprep": [
            random.uniform(0, 100) for _ in range(size)
        ],
        "pctconfc19hosppatsicuadultperchosprep": [
            random.uniform(0, 100) for _ in range(size)
        ],
        "pctconfc19hosppatsicupedperchosprep": [
            random.uniform(0, 100) for _ in range(size)
        ],
        "pctconffluhosppatsicuperchosprep": [
            random.uniform(0, 100) for _ in range(size)
        ],
        "pctconffluhosppatsicuadultperchosprep": [
            random.uniform(0, 100) for _ in range(size)
        ],
        "pctconffluhosppatsicupedperchosprep": [
            random.uniform(0, 100) for _ in range(size)
        ],
        "pctconfrsvhosppatsicuperchosprep": [
            random.uniform(0, 100) for _ in range(size)
        ],
        "pctconfrsvhosppatsicuadultperchosprep": [
            random.uniform(0, 100) for _ in range(size)
        ],
        "pctconfrsvhosppatsicupedperchosprep": [
            random.uniform(0, 100) for _ in range(size)
        ],
        "pctinptbedsoccadultperchosprepabschg": [
            random.uniform(-100, 100) for _ in range(size)
        ],
        "pctinptbedsoccpedperchosprepabschg": [
            random.uniform(-100, 100) for _ in range(size)
        ],
        "pcticubedsoccadultperchosprepabschg": [
            random.uniform(-100, 100) for _ in range(size)
        ],
        "pcticubedsoccpedperchosprepabschg": [
            random.uniform(-100, 100) for _ in range(size)
        ],
        "pctconfc19inptbedsadultperchosprepabschg": [
            random.uniform(-100, 100) for _ in range(size)
        ],
        "pctconfc19inptbedspedperchosprepabschg": [
            random.uniform(-100, 100) for _ in range(size)
        ],
        "pctconfc19icubedsadultperchosprepabschg": [
            random.uniform(-100, 100) for _ in range(size)
        ],
        "pctconfc19icubedspedperchosprepabschg": [
            random.uniform(-100, 100) for _ in range(size)
        ],
        "pctconffluinptbedsadultperchosprepabschg": [
            random.uniform(-100, 100) for _ in range(size)
        ],
        "pctconffluinptbedspedperchosprepabschg": [
            random.uniform(-100, 100) for _ in range(size)
        ],
        "pctconffluicubedsadultperchosprepabschg": [
            random.uniform(-100, 100) for _ in range(size)
        ],
        "pctconffluicubedspedperchosprepabschg": [
            random.uniform(-100, 100) for _ in range(size)
        ],
        "pctconfrsvinptbedsadultperchosprepabschg": [
            random.uniform(-100, 100) for _ in range(size)
        ],
        "pctconfrsvinptbedspedperchosprepabschg": [
            random.uniform(-100, 100) for _ in range(size)
        ],
        "pctconfrsvicubedsadultperchosprepabschg": [
            random.uniform(-100, 100) for _ in range(size)
        ],
        "pctconfrsvicubedspedperchosprepabschg": [
            random.uniform(-100, 100) for _ in range(size)
        ],
        "pctconfc19hosppatsicuperchosprepabschg": [
            random.uniform(-100, 100) for _ in range(size)
        ],
        "pctconfc19hosppatsicuadultperchosprepabschg": [
            random.uniform(-100, 100) for _ in range(size)
        ],
        "pctconfc19hosppatsicupedperchosprepabschg": [
            random.uniform(-100, 100) for _ in range(size)
        ],
        "pctconffluhosppatsicuperchosprepabschg": [
            random.uniform(-100, 100) for _ in range(size)
        ],
        "pctconffluhosppatsicuadultperchosprepabschg": [
            random.uniform(-100, 100) for _ in range(size)
        ],
        "pctconffluhosppatsicupedperchosprepabschg": [
            random.uniform(-100, 100) for _ in range(size)
        ],
        "pctconfrsvhosppatsicuperchosprepabschg": [
            random.uniform(-100, 100) for _ in range(size)
        ],
        "pctconfrsvhosppatsicuadultperchosprepabschg": [
            random.uniform(-100, 100) for _ in range(size)
        ],
        "pctconfrsvhosppatsicupedperchosprepabschg": [
            random.uniform(-100, 100) for _ in range(size)
        ],
        "respseason": [None for _ in range(size)],
        "totalconfc19newadmcumulativeseasonalsum": [
            random.uniform(0, 100000) for _ in range(size)
        ],
        "totalconfflunewadmcumulativeseasonalsum": [
            random.uniform(0, 100000) for _ in range(size)
        ],
        "totalconfrsvnewadmcumulativeseasonalsum": [
            random.uniform(0, 100000) for _ in range(size)
        ],
        "totalconfnewadmcumulativeseasonalsum": [
            random.uniform(0, 100000) for _ in range(size)
        ],
        "numconfc19icupatsped": [
            random.uniform(0, 10000) for _ in range(size)
        ],
        "numconfc19newadmped5to17": [
            random.uniform(0, 10000) for _ in range(size)
        ],
        "numconfc19newadmped5to17per100k": [
            random.uniform(0, 100) for _ in range(size)
        ],
        "pctconfc19icubedsped": [random.uniform(0, 100) for _ in range(size)],
        "pctconfc19hosppatsicuped": [
            random.uniform(0, 100) for _ in range(size)
        ],
        "numconfc19newadmped0to4": [
            random.uniform(0, 10000) for _ in range(size)
        ],
        "numconfc19newadmped0to4per100k": [
            random.uniform(0, 100) for _ in range(size)
        ],
        "numconfc19newadmped0to4pctchg": [
            random.uniform(-100, 100) for _ in range(size)
        ],
        "numconfc19newadmped5to17pctchg": [
            random.uniform(-100, 100) for _ in range(size)
        ],
        "numconffluhosppatsadult": [
            random.uniform(0, 50000) for _ in range(size)
        ],
        "numconffluhosppatsped": [
            random.uniform(0, 10000) for _ in range(size)
        ],
        "numconfrsvhosppatsadult": [
            random.uniform(0, 50000) for _ in range(size)
        ],
        "numconfrsvhosppatsped": [
            random.uniform(0, 10000) for _ in range(size)
        ],
        "totalconfrsvhosppats": [
            random.uniform(0, 60000) for _ in range(size)
        ],
        "numconffluicupatsadult": [
            random.uniform(0, 10000) for _ in range(size)
        ],
        "numconffluicupatsped": [random.uniform(0, 5000) for _ in range(size)],
        "numconfrsvicupatsadult": [
            random.uniform(0, 10000) for _ in range(size)
        ],
        "numconfrsvicupatsped": [random.uniform(0, 5000) for _ in range(size)],
        "totalconfrsvicupats": [random.uniform(0, 15000) for _ in range(size)],
        "numconfc19newadmadult50to64": [
            random.uniform(0, 10000) for _ in range(size)
        ],
        "numconfc19newadmadult65to74": [
            random.uniform(0, 10000) for _ in range(size)
        ],
        "numconfc19newadmadult75plus": [
            random.uniform(0, 10000) for _ in range(size)
        ],
        "numconfflunewadmped0to4": [
            random.uniform(0, 5000) for _ in range(size)
        ],
        "numconfflunewadmped5to17": [
            random.uniform(0, 5000) for _ in range(size)
        ],
        "totalconfflunewadmped": [
            random.uniform(0, 10000) for _ in range(size)
        ],
        "numconfflunewadmadult18to49": [
            random.uniform(0, 15000) for _ in range(size)
        ],
        "numconfflunewadmadult50to64": [
            random.uniform(0, 10000) for _ in range(size)
        ],
        "numconfflunewadmadult65to74": [
            random.uniform(0, 10000) for _ in range(size)
        ],
        "numconfflunewadmadult75plus": [
            random.uniform(0, 10000) for _ in range(size)
        ],
        "totalconfflunewadmadult": [
            random.uniform(0, 30000) for _ in range(size)
        ],
        "numconfflunewadmunk": [random.uniform(0, 5000) for _ in range(size)],
        "numconfrsvnewadmped0to4": [
            random.uniform(0, 5000) for _ in range(size)
        ],
        "numconfrsvnewadmped5to17": [
            random.uniform(0, 5000) for _ in range(size)
        ],
        "totalconfrsvnewadmped": [
            random.uniform(0, 10000) for _ in range(size)
        ],
        "numconfrsvnewadmadult18to49": [
            random.uniform(0, 15000) for _ in range(size)
        ],
        "numconfrsvnewadmadult50to64": [
            random.uniform(0, 10000) for _ in range(size)
        ],
        "numconfrsvnewadmadult65to74": [
            random.uniform(0, 10000) for _ in range(size)
        ],
        "numconfrsvnewadmadult75plus": [
            random.uniform(0, 10000) for _ in range(size)
        ],
        "totalconfrsvnewadmadult": [
            random.uniform(0, 30000) for _ in range(size)
        ],
        "numconfrsvnewadmunk": [random.uniform(0, 5000) for _ in range(size)],
        "totalconfrsvnewadm": [random.uniform(0, 40000) for _ in range(size)],
        "pctconfrsvinptbeds": [random.uniform(0, 100) for _ in range(size)],
        "pctconfrsvicubeds": [random.uniform(0, 100) for _ in range(size)],
        "pctconfflunewadmadult": [random.uniform(0, 100) for _ in range(size)],
        "pctconfflunewadmped": [random.uniform(0, 100) for _ in range(size)],
        "pctconfrsvnewadmadult": [random.uniform(0, 100) for _ in range(size)],
        "pctconfrsvnewadmped": [random.uniform(0, 100) for _ in range(size)],
        "numconfc19newadmadult50to64per100k": [
            random.uniform(0, 100) for _ in range(size)
        ],
        "numconfc19newadmadult65to74per100k": [
            random.uniform(0, 100) for _ in range(size)
        ],
        "numconfc19newadmadult75plusper100k": [
            random.uniform(0, 100) for _ in range(size)
        ],
        "numconfflunewadmped0to4per100k": [
            random.uniform(0, 100) for _ in range(size)
        ],
        "numconfflunewadmped5to17per100k": [
            random.uniform(0, 100) for _ in range(size)
        ],
        "totalconfflunewadmpedper100k": [
            random.uniform(0, 100) for _ in range(size)
        ],
        "numconfflunewadmadult18to49per100k": [
            random.uniform(0, 100) for _ in range(size)
        ],
        "numconfflunewadmadult50to64per100k": [
            random.uniform(0, 100) for _ in range(size)
        ],
        "numconfflunewadmadult65to74per100k": [
            random.uniform(0, 100) for _ in range(size)
        ],
        "numconfflunewadmadult75plusper100k": [
            random.uniform(0, 100) for _ in range(size)
        ],
        "totalconfflunewadmadultper100k": [
            random.uniform(0, 100) for _ in range(size)
        ],
        "numconfrsvnewadmped0to4per100k": [
            random.uniform(0, 100) for _ in range(size)
        ],
        "numconfrsvnewadmped5to17per100k": [
            random.uniform(0, 100) for _ in range(size)
        ],
        "totalconfrsvnewadmpedper100k": [
            random.uniform(0, 100) for _ in range(size)
        ],
        "numconfrsvnewadmadult18to49per100k": [
            random.uniform(0, 100) for _ in range(size)
        ],
        "numconfrsvnewadmadult50to64per100k": [
            random.uniform(0, 100) for _ in range(size)
        ],
        "numconfrsvnewadmadult65to74per100k": [
            random.uniform(0, 100) for _ in range(size)
        ],
        "numconfrsvnewadmadult75plusper100k": [
            random.uniform(0, 100) for _ in range(size)
        ],
        "totalconfrsvnewadmadultper100k": [
            random.uniform(0, 100) for _ in range(size)
        ],
        "totalconfrsvnewadmper100k": [
            random.uniform(0, 100) for _ in range(size)
        ],
        "pctconffluinptbedsadult": [
            random.uniform(0, 100) for _ in range(size)
        ],
        "pctconffluinptbedsped": [random.uniform(0, 100) for _ in range(size)],
        "pctconffluicubedsadult": [
            random.uniform(0, 100) for _ in range(size)
        ],
        "pctconffluicubedsped": [random.uniform(0, 100) for _ in range(size)],
        "pctconfrsvinptbedsadult": [
            random.uniform(0, 100) for _ in range(size)
        ],
        "pctconfrsvinptbedsped": [random.uniform(0, 100) for _ in range(size)],
        "pctconfrsvicubedsadult": [
            random.uniform(0, 100) for _ in range(size)
        ],
        "pctconfrsvicubedsped": [random.uniform(0, 100) for _ in range(size)],
        "pctconffluhosppatsicuadult": [
            random.uniform(0, 100) for _ in range(size)
        ],
        "pctconfrsvhosppatsicu": [random.uniform(0, 100) for _ in range(size)],
        "pctconfrsvhosppatsicuadult": [
            random.uniform(0, 100) for _ in range(size)
        ],
        "pctconfrsvhosppatsicuped": [
            random.uniform(0, 100) for _ in range(size)
        ],
        "numconfc19newadmadult50to64pctchg": [
            random.uniform(-100, 100) for _ in range(size)
        ],
        "numconfc19newadmadult65to74pctchg": [
            random.uniform(-100, 100) for _ in range(size)
        ],
        "numconfc19newadmadult75pluspctchg": [
            random.uniform(-100, 100) for _ in range(size)
        ],
        "numconfflunewadmped5to17pctchg": [
            random.uniform(-100, 100) for _ in range(size)
        ],
        "totalconfflunewadmpedpctchg": [
            random.uniform(-100, 100) for _ in range(size)
        ],
        "numconfflunewadmadult18to49pctchg": [
            random.uniform(-100, 100) for _ in range(size)
        ],
        "numconfflunewadmadult50to64pctchg": [
            random.uniform(-100, 100) for _ in range(size)
        ],
        "numconfflunewadmadult65to74pctchg": [
            random.uniform(-100, 100) for _ in range(size)
        ],
        "numconfflunewadmadult75pluspctchg": [
            random.uniform(-100, 100) for _ in range(size)
        ],
        "totalconfflunewadmadultpctchg": [
            random.uniform(-100, 100) for _ in range(size)
        ],
        "numconfrsvnewadmped0to4pctchg": [
            random.uniform(-100, 100) for _ in range(size)
        ],
        "numconfrsvnewadmped5to17pctchg": [
            random.uniform(-100, 100) for _ in range(size)
        ],
        "totalconfrsvnewadmpedpctchg": [
            random.uniform(-100, 100) for _ in range(size)
        ],
        "numconfrsvnewadmadult18to49pctchg": [
            random.uniform(-100, 100) for _ in range(size)
        ],
        "numconfrsvnewadmadult50to64pctchg": [
            random.uniform(-100, 100) for _ in range(size)
        ],
        "totalconfrsvnewadmadultpctchg": [
            random.uniform(-100, 100) for _ in range(size)
        ],
        "totalconfrsvnewadmpctchg": [
            random.uniform(-100, 100) for _ in range(size)
        ],
        "numconfrsvnewadmadult75pluspctchg": [
            random.uniform(-100, 100) for _ in range(size)
        ],
        "numconfrsvnewadmadult65to74pctchg": [
            random.uniform(-100, 100) for _ in range(size)
        ],
        "pctconffluhosppatsicuped": [
            random.uniform(0, 100) for _ in range(size)
        ],
        "numconfflunewadmped0to4pctchg": [
            random.uniform(-100, 100) for _ in range(size)
        ],
    }
    df = pd.DataFrame(data)
    return df if output == "pandas" or output == "pd" else pl.from_pandas(df)


def load_mock_data(output="pandas", size=10) -> pd.DataFrame | pl.DataFrame:
    data = {
        "weekendingdate": [str(fake.date()) for _ in range(size)],
        "jurisdiction": [random.choice(region_opts) for _ in range(size)],
        "numinptbeds": [random.uniform(7, 831870) for _ in range(size)],
        "numinptbedsadult": [random.uniform(3, 743870) for _ in range(size)],
        "numinptbedsped": [random.uniform(0, 84581) for _ in range(size)],
        "numinptbedsocc": [random.uniform(0, 587461) for _ in range(size)],
        "numinptbedsoccadult": [
            random.uniform(0, 543870) for _ in range(size)
        ],
        "numinptbedsoccped": [random.uniform(0, 84581) for _ in range(size)],
        "numicubeds": [random.uniform(0, 100000) for _ in range(size)],
        "numicubedsadult": [random.uniform(0, 90000) for _ in range(size)],
        "numicubedsped": [random.uniform(0, 10000) for _ in range(size)],
        "numicubedsocc": [random.uniform(0, 90000) for _ in range(size)],
        "numicubedsoccadult": [random.uniform(0, 80000) for _ in range(size)],
        "numicubedsoccped": [random.uniform(0, 10000) for _ in range(size)],
        "numconfc19hosppatsadult": [
            random.uniform(0, 50000) for _ in range(size)
        ],
        "numconfc19hosppatsped": [
            random.uniform(0, 10000) for _ in range(size)
        ],
        "totalconfc19hosppats": [
            random.uniform(0, 60000) for _ in range(size)
        ],
        "totalconffluhosppats": [
            random.uniform(0, 50000) for _ in range(size)
        ],
        "numconfc19icupatsadult": [
            random.uniform(0, 10000) for _ in range(size)
        ],
        "totalconfc19icupats": [random.uniform(0, 15000) for _ in range(size)],
        "totalconffluicupats": [random.uniform(0, 12000) for _ in range(size)],
        "totalconfc19newadmped": [
            random.uniform(0, 10000) for _ in range(size)
        ],
        "numconfc19newadmadult18to49": [
            random.uniform(0, 20000) for _ in range(size)
        ],
        "totalconfc19newadmadult": [
            random.uniform(0, 30000) for _ in range(size)
        ],
        "numconfc19newadmunk": [random.uniform(0, 5000) for _ in range(size)],
        "totalconfc19newadm": [random.uniform(0, 40000) for _ in range(size)],
        "totalconfflunewadm": [random.uniform(0, 35000) for _ in range(size)],
        "pctinptbedsocc": [random.uniform(0, 100) for _ in range(size)],
        "pctconfc19inptbeds": [random.uniform(0, 100) for _ in range(size)],
        "pctconffluinptbeds": [random.uniform(0, 100) for _ in range(size)],
        "pcticubedsocc": [random.uniform(0, 100) for _ in range(size)],
        "pctconfc19icubeds": [random.uniform(0, 100) for _ in range(size)],
        "pctconffluicubeds": [random.uniform(0, 100) for _ in range(size)],
        "pctconfc19newadmadult": [random.uniform(0, 100) for _ in range(size)],
        "pctconfc19newadmped": [random.uniform(0, 100) for _ in range(size)],
        "numinptbedshosprep": [random.uniform(0, 500000) for _ in range(size)],
        "numinptbedsocchosprep": [
            random.uniform(0, 400000) for _ in range(size)
        ],
        "numicubedshosprep": [random.uniform(0, 100000) for _ in range(size)],
        "numicubedsocchosprep": [
            random.uniform(0, 90000) for _ in range(size)
        ],
        "totalconfc19hosppatshosprep": [
            random.uniform(0, 60000) for _ in range(size)
        ],
        "totalconffluhosppatshosprep": [
            random.uniform(0, 50000) for _ in range(size)
        ],
        "totalconfrsvhosppatshosprep": [
            random.uniform(0, 40000) for _ in range(size)
        ],
        "totalconfc19icupatshosprep": [
            random.uniform(0, 15000) for _ in range(size)
        ],
        "totalconffluicupatshosprep": [
            random.uniform(0, 12000) for _ in range(size)
        ],
        "totalconfrsvicupatshosprep": [
            random.uniform(0, 10000) for _ in range(size)
        ],
        "totalconfc19newadmpedhosprep": [
            random.uniform(0, 10000) for _ in range(size)
        ],
        "totalconfc19newadmadulthosprep": [
            random.uniform(0, 30000) for _ in range(size)
        ],
        "totalconfc19newadmhosprep": [
            random.uniform(0, 40000) for _ in range(size)
        ],
        "totalconfflunewadmpedhosprep": [
            random.uniform(0, 35000) for _ in range(size)
        ],
        "totalconfflunewadmadulthosprep": [
            random.uniform(0, 35000) for _ in range(size)
        ],
        "totalconfflunewadmhosprep": [
            random.uniform(0, 40000) for _ in range(size)
        ],
        "totalconfrsvnewadmpedhosprep": [
            random.uniform(0, 30000) for _ in range(size)
        ],
        "totalconfrsvnewadmadulthosprep": [
            random.uniform(0, 30000) for _ in range(size)
        ],
        "totalconfrsvnewadmhosprep": [
            random.uniform(0, 35000) for _ in range(size)
        ],
        "pctinptbedsocchosprep": [random.uniform(0, 100) for _ in range(size)],
        "pcticubedsocchosprep": [random.uniform(0, 100) for _ in range(size)],
        "pctconfc19inptbedshosprep": [
            random.uniform(0, 100) for _ in range(size)
        ],
        "pctconffluinptbedshosprep": [
            random.uniform(0, 100) for _ in range(size)
        ],
        "pctconfrsvinptbedshosprep": [
            random.uniform(0, 100) for _ in range(size)
        ],
        "pctconfc19icubedshosprep": [
            random.uniform(0, 100) for _ in range(size)
        ],
        "pctconffluicubedshosprep": [
            random.uniform(0, 100) for _ in range(size)
        ],
        "pctconfrsvicubedshosprep": [
            random.uniform(0, 100) for _ in range(size)
        ],
        "numinptbedsperchosprep": [
            random.uniform(0, 1000) for _ in range(size)
        ],
        "numinptbedsoccperchosprep": [
            random.uniform(0, 1000) for _ in range(size)
        ],
        "numicubedsperchosprep": [random.uniform(0, 500) for _ in range(size)],
        "numicubedsoccperchosprep": [
            random.uniform(0, 500) for _ in range(size)
        ],
        "totalconfc19hosppatsperc": [
            random.uniform(0, 100) for _ in range(size)
        ],
        "totalconffluhosppatsperc": [
            random.uniform(0, 100) for _ in range(size)
        ],
        "totalconfrsvhosppatsperc": [
            random.uniform(0, 100) for _ in range(size)
        ],
        "totalconfc19icupatsperchosprep": [
            random.uniform(0, 100) for _ in range(size)
        ],
        "totalconffluicupatsperchosprep": [
            random.uniform(0, 100) for _ in range(size)
        ],
        "totalconfrsvicupatsperchosprep": [
            random.uniform(0, 100) for _ in range(size)
        ],
        "totalconfc19newadmpedper": [
            random.uniform(0, 100) for _ in range(size)
        ],
        "totalconfc19newadmadultp": [
            random.uniform(0, 100) for _ in range(size)
        ],
        "totalconfc19newadmperchosprep": [
            random.uniform(0, 100) for _ in range(size)
        ],
        "totalconfflunewadmpedper": [
            random.uniform(0, 100) for _ in range(size)
        ],
        "totalconfflunewadmadultp": [
            random.uniform(0, 100) for _ in range(size)
        ],
        "totalconfflunewadmperchosprep": [
            random.uniform(0, 100) for _ in range(size)
        ],
        "totalconfrsvnewadmpedper": [
            random.uniform(0, 100) for _ in range(size)
        ],
        "totalconfrsvnewadmadultp": [
            random.uniform(0, 100) for _ in range(size)
        ],
        "totalconfrsvnewadmperchosprep": [
            random.uniform(0, 100) for _ in range(size)
        ],
        "pctinptbedsoccperchosprep": [
            random.uniform(0, 100) for _ in range(size)
        ],
        "pcticubedsoccperchosprep": [
            random.uniform(0, 100) for _ in range(size)
        ],
        "pctconfc19inptbedsperchosprep": [
            random.uniform(0, 100) for _ in range(size)
        ],
        "pctconffluinptbedsperchosprep": [
            random.uniform(0, 100) for _ in range(size)
        ],
        "pctconfrsvinptbedsperchosprep": [
            random.uniform(0, 100) for _ in range(size)
        ],
        "pctconfc19icubedsperchosprep": [
            random.uniform(0, 100) for _ in range(size)
        ],
        "pctconffluicubedsperchosprep": [
            random.uniform(0, 100) for _ in range(size)
        ],
        "pctconfrsvicubedsperchosprep": [
            random.uniform(0, 100) for _ in range(size)
        ],
        "numinptbedsperchosprepabschg": [
            random.uniform(0, 1000) for _ in range(size)
        ],
        "numinptbedsoccperchospre": [
            random.uniform(0, 1000) for _ in range(size)
        ],
        "numicubedsperchosprepabschg": [
            random.uniform(0, 500) for _ in range(size)
        ],
        "numicubedsoccperchosprepabschg": [
            random.uniform(0, 500) for _ in range(size)
        ],
        "totalconfc19hosppatsperc_1": [
            random.uniform(0, 100) for _ in range(size)
        ],
        "totalconffluhosppatsperc_1": [
            random.uniform(0, 100) for _ in range(size)
        ],
        "totalconfrsvhosppatsperc_1": [
            random.uniform(0, 100) for _ in range(size)
        ],
        "totalconfc19icupatsperch": [
            random.uniform(0, 100) for _ in range(size)
        ],
        "totalconffluicupatsperch": [
            random.uniform(0, 100) for _ in range(size)
        ],
        "totalconfrsvicupatsperch": [
            random.uniform(0, 100) for _ in range(size)
        ],
        "totalconfc19newadmpedper_1": [
            random.uniform(0, 100) for _ in range(size)
        ],
        "totalconfc19newadmadultp_1": [
            random.uniform(0, 100) for _ in range(size)
        ],
        "totalconfc19newadmpercho": [
            random.uniform(0, 100) for _ in range(size)
        ],
        "totalconfflunewadmpedper_1": [
            random.uniform(0, 100) for _ in range(size)
        ],
        "totalconfflunewadmadultp_1": [
            random.uniform(0, 100) for _ in range(size)
        ],
        "totalconfflunewadmpercho": [
            random.uniform(0, 100) for _ in range(size)
        ],
        "totalconfrsvnewadmpedper_1": [
            random.uniform(0, 100) for _ in range(size)
        ],
        "totalconfrsvnewadmadultp_1": [
            random.uniform(0, 100) for _ in range(size)
        ],
        "totalconfrsvnewadmpercho": [
            random.uniform(0, 100) for _ in range(size)
        ],
        "pctinptbedsoccperchospre": [
            random.uniform(0, 100) for _ in range(size)
        ],
        "pcticubedsoccperchosprepabschg": [
            random.uniform(0, 100) for _ in range(size)
        ],
        "pctconfc19inptbedspercho": [
            random.uniform(0, 100) for _ in range(size)
        ],
        "pctconffluinptbedspercho": [
            random.uniform(0, 100) for _ in range(size)
        ],
        "pctconfrsvinptbedspercho": [
            random.uniform(0, 100) for _ in range(size)
        ],
        "pctconfc19icubedsperchos": [
            random.uniform(0, 100) for _ in range(size)
        ],
        "pctconffluicubedsperchos": [
            random.uniform(0, 100) for _ in range(size)
        ],
        "pctconfrsvicubedsperchos": [
            random.uniform(0, 100) for _ in range(size)
        ],
        "totalconfc19newadmpedper100k": [
            random.uniform(0, 100) for _ in range(size)
        ],
        "numconfc19newadmadult18to49per100k": [
            random.uniform(0, 100) for _ in range(size)
        ],
        "totalconfc19newadmadultper100k": [
            random.uniform(0, 100) for _ in range(size)
        ],
        "totalconfc19newadmper100k": [
            random.uniform(0, 100) for _ in range(size)
        ],
        "totalconfflunewadmper100k": [
            random.uniform(0, 100) for _ in range(size)
        ],
        "totalconfc19newadmperchosprepabove80pct": [
            random.uniform(0, 100) for _ in range(size)
        ],
        "totalconfc19newadmperchosprepabove90pct": [
            random.uniform(0, 100) for _ in range(size)
        ],
        "totalconfflunewadmperchosprepabove80pct": [
            random.uniform(0, 100) for _ in range(size)
        ],
        "totalconfflunewadmperchosprepabove90pct": [
            random.uniform(0, 100) for _ in range(size)
        ],
        "totalconfrsvnewadmperchosprepabove80pct": [
            random.uniform(0, 100) for _ in range(size)
        ],
        "totalconfrsvnewadmperchosprepabove90pct": [
            random.uniform(0, 100) for _ in range(size)
        ],
        "pctinptbedsoccadult": [random.uniform(0, 100) for _ in range(size)],
        "pctinptbedsoccped": [random.uniform(0, 100) for _ in range(size)],
        "pcticubedsoccadult": [random.uniform(0, 100) for _ in range(size)],
        "pcticubedsoccped": [random.uniform(0, 100) for _ in range(size)],
        "pctconfc19inptbedsadult": [
            random.uniform(0, 100) for _ in range(size)
        ],
        "pctconfc19inptbedsped": [random.uniform(0, 100) for _ in range(size)],
        "pctconfc19icubedsadult": [
            random.uniform(0, 100) for _ in range(size)
        ],
        "pctconfc19hosppatsicu": [random.uniform(0, 100) for _ in range(size)],
        "pctconfc19hosppatsicuadult": [
            random.uniform(0, 100) for _ in range(size)
        ],
        "pctconffluhosppatsicu": [random.uniform(0, 100) for _ in range(size)],
        "totalconfc19newadmpedpctchg": [
            random.uniform(-100, 100) for _ in range(size)
        ],
        "numconfc19newadmadult18to49pctchg": [
            random.uniform(-100, 100) for _ in range(size)
        ],
        "totalconfc19newadmadultpctchg": [
            random.uniform(-100, 100) for _ in range(size)
        ],
        "totalconfc19newadmpctchg": [
            random.uniform(-100, 100) for _ in range(size)
        ],
        "totalconfflunewadmpctchg": [
            random.uniform(-100, 100) for _ in range(size)
        ],
        "pctinptbedsoccadulthosprep": [
            random.uniform(0, 100) for _ in range(size)
        ],
        "pctinptbedsoccpedhosprep": [
            random.uniform(0, 100) for _ in range(size)
        ],
        "pcticubedsoccadulthosprep": [
            random.uniform(0, 100) for _ in range(size)
        ],
        "pcticubedsoccpedhosprep": [
            random.uniform(0, 100) for _ in range(size)
        ],
        "pctconfc19inptbedsadulthosprep": [
            random.uniform(0, 100) for _ in range(size)
        ],
        "pctconfc19inptbedspedhosprep": [
            random.uniform(0, 100) for _ in range(size)
        ],
        "pctconfc19icubedsadulthosprep": [
            random.uniform(0, 100) for _ in range(size)
        ],
        "pctconfc19icubedspedhosprep": [
            random.uniform(0, 100) for _ in range(size)
        ],
        "pctconffluinptbedsadulthosprep": [
            random.uniform(0, 100) for _ in range(size)
        ],
        "pctconffluinptbedspedhosprep": [
            random.uniform(0, 100) for _ in range(size)
        ],
        "pctconffluicubedsadulthosprep": [
            random.uniform(0, 100) for _ in range(size)
        ],
        "pctconffluicubedspedhosprep": [
            random.uniform(0, 100) for _ in range(size)
        ],
        "pctconfrsvinptbedsadulthosprep": [
            random.uniform(0, 100) for _ in range(size)
        ],
        "pctconfrsvinptbedspedhosprep": [
            random.uniform(0, 100) for _ in range(size)
        ],
        "pctconfrsvicubedsadulthosprep": [
            random.uniform(0, 100) for _ in range(size)
        ],
        "pctconfrsvicubedspedhosprep": [
            random.uniform(0, 100) for _ in range(size)
        ],
        "pctconfc19hosppatsicuhosprep": [
            random.uniform(0, 100) for _ in range(size)
        ],
        "pctconfc19hosppatsicuadulthosprep": [
            random.uniform(0, 100) for _ in range(size)
        ],
        "pctconfc19hosppatsicupedhosprep": [
            random.uniform(0, 100) for _ in range(size)
        ],
        "pctconffluhosppatsicuhosprep": [
            random.uniform(0, 100) for _ in range(size)
        ],
        "pctconffluhosppatsicuadulthosprep": [
            random.uniform(0, 100) for _ in range(size)
        ],
        "pctconffluhosppatsicupedhosprep": [
            random.uniform(0, 100) for _ in range(size)
        ],
        "pctconfrsvhosppatsicuhosprep": [
            random.uniform(0, 100) for _ in range(size)
        ],
        "pctconfrsvhosppatsicuadulthosprep": [
            random.uniform(0, 100) for _ in range(size)
        ],
        "pctconfrsvhosppatsicupedhosprep": [
            random.uniform(0, 100) for _ in range(size)
        ],
        "pctinptbedsoccadultperchosprep": [
            random.uniform(0, 100) for _ in range(size)
        ],
        "pctinptbedsoccpedperchosprep": [
            random.uniform(0, 100) for _ in range(size)
        ],
        "pcticubedsoccadultperchosprep": [
            random.uniform(0, 100) for _ in range(size)
        ],
        "pcticubedsoccpedperchosprep": [
            random.uniform(0, 100) for _ in range(size)
        ],
        "pctconfc19inptbedsadultperchosprep": [
            random.uniform(0, 100) for _ in range(size)
        ],
        "pctconfc19inptbedspedperchosprep": [
            random.uniform(0, 100) for _ in range(size)
        ],
        "pctconfc19icubedsadultperchosprep": [
            random.uniform(0, 100) for _ in range(size)
        ],
        "pctconfc19icubedspedperchosprep": [
            random.uniform(0, 100) for _ in range(size)
        ],
        "pctconffluinptbedsadultperchosprep": [
            random.uniform(0, 100) for _ in range(size)
        ],
        "pctconffluinptbedspedperchosprep": [
            random.uniform(0, 100) for _ in range(size)
        ],
        "pctconffluicubedsadultperchosprep": [
            random.uniform(0, 100) for _ in range(size)
        ],
        "pctconffluicubedspedperchosprep": [
            random.uniform(0, 100) for _ in range(size)
        ],
        "pctconfrsvinptbedsadultperchosprep": [
            random.uniform(0, 100) for _ in range(size)
        ],
        "pctconfrsvinptbedspedperchosprep": [
            random.uniform(0, 100) for _ in range(size)
        ],
        "pctconfrsvicubedsadultperchosprep": [
            random.uniform(0, 100) for _ in range(size)
        ],
        "pctconfrsvicubedspedperchosprep": [
            random.uniform(0, 100) for _ in range(size)
        ],
        "pctconfc19hosppatsicuperchosprep": [
            random.uniform(0, 100) for _ in range(size)
        ],
        "pctconfc19hosppatsicuadultperchosprep": [
            random.uniform(0, 100) for _ in range(size)
        ],
        "pctconfc19hosppatsicupedperchosprep": [
            random.uniform(0, 100) for _ in range(size)
        ],
        "pctconffluhosppatsicuperchosprep": [
            random.uniform(0, 100) for _ in range(size)
        ],
        "pctconffluhosppatsicuadultperchosprep": [
            random.uniform(0, 100) for _ in range(size)
        ],
        "pctconffluhosppatsicupedperchosprep": [
            random.uniform(0, 100) for _ in range(size)
        ],
        "pctconfrsvhosppatsicuperchosprep": [
            random.uniform(0, 100) for _ in range(size)
        ],
        "pctconfrsvhosppatsicuadultperchosprep": [
            random.uniform(0, 100) for _ in range(size)
        ],
        "pctconfrsvhosppatsicupedperchosprep": [
            random.uniform(0, 100) for _ in range(size)
        ],
        "pctinptbedsoccadultperchosprepabschg": [
            random.uniform(-100, 100) for _ in range(size)
        ],
        "pctinptbedsoccpedperchosprepabschg": [
            random.uniform(-100, 100) for _ in range(size)
        ],
        "pcticubedsoccadultperchosprepabschg": [
            random.uniform(-100, 100) for _ in range(size)
        ],
        "pcticubedsoccpedperchosprepabschg": [
            random.uniform(-100, 100) for _ in range(size)
        ],
        "pctconfc19inptbedsadultperchosprepabschg": [
            random.uniform(-100, 100) for _ in range(size)
        ],
        "pctconfc19inptbedspedperchosprepabschg": [
            random.uniform(-100, 100) for _ in range(size)
        ],
        "pctconfc19icubedsadultperchosprepabschg": [
            random.uniform(-100, 100) for _ in range(size)
        ],
        "pctconfc19icubedspedperchosprepabschg": [
            random.uniform(-100, 100) for _ in range(size)
        ],
        "pctconffluinptbedsadultperchosprepabschg": [
            random.uniform(-100, 100) for _ in range(size)
        ],
        "pctconffluinptbedspedperchosprepabschg": [
            random.uniform(-100, 100) for _ in range(size)
        ],
        "pctconffluicubedsadultperchosprepabschg": [
            random.uniform(-100, 100) for _ in range(size)
        ],
        "pctconffluicubedspedperchosprepabschg": [
            random.uniform(-100, 100) for _ in range(size)
        ],
        "pctconfrsvinptbedsadultperchosprepabschg": [
            random.uniform(-100, 100) for _ in range(size)
        ],
        "pctconfrsvinptbedspedperchosprepabschg": [
            random.uniform(-100, 100) for _ in range(size)
        ],
        "pctconfrsvicubedsadultperchosprepabschg": [
            random.uniform(-100, 100) for _ in range(size)
        ],
        "pctconfrsvicubedspedperchosprepabschg": [
            random.uniform(-100, 100) for _ in range(size)
        ],
        "pctconfc19hosppatsicuperchosprepabschg": [
            random.uniform(-100, 100) for _ in range(size)
        ],
        "pctconfc19hosppatsicuadultperchosprepabschg": [
            random.uniform(-100, 100) for _ in range(size)
        ],
        "pctconfc19hosppatsicupedperchosprepabschg": [
            random.uniform(-100, 100) for _ in range(size)
        ],
        "pctconffluhosppatsicuperchosprepabschg": [
            random.uniform(-100, 100) for _ in range(size)
        ],
        "pctconffluhosppatsicuadultperchosprepabschg": [
            random.uniform(-100, 100) for _ in range(size)
        ],
        "pctconffluhosppatsicupedperchosprepabschg": [
            random.uniform(-100, 100) for _ in range(size)
        ],
        "pctconfrsvhosppatsicuperchosprepabschg": [
            random.uniform(-100, 100) for _ in range(size)
        ],
        "pctconfrsvhosppatsicuadultperchosprepabschg": [
            random.uniform(-100, 100) for _ in range(size)
        ],
        "pctconfrsvhosppatsicupedperchosprepabschg": [
            random.uniform(-100, 100) for _ in range(size)
        ],
        "respseason": [None for _ in range(size)],
        "totalconfc19newadmcumulativeseasonalsum": [
            random.uniform(0, 100000) for _ in range(size)
        ],
        "totalconfflunewadmcumulativeseasonalsum": [
            random.uniform(0, 100000) for _ in range(size)
        ],
        "totalconfrsvnewadmcumulativeseasonalsum": [
            random.uniform(0, 100000) for _ in range(size)
        ],
        "totalconfnewadmcumulativeseasonalsum": [
            random.uniform(0, 100000) for _ in range(size)
        ],
        "numconfc19icupatsped": [
            random.uniform(0, 10000) for _ in range(size)
        ],
        "numconfc19newadmped5to17": [
            random.uniform(0, 10000) for _ in range(size)
        ],
        "numconfc19newadmped5to17per100k": [
            random.uniform(0, 100) for _ in range(size)
        ],
        "pctconfc19icubedsped": [random.uniform(0, 100) for _ in range(size)],
        "pctconfc19hosppatsicuped": [
            random.uniform(0, 100) for _ in range(size)
        ],
        "numconfc19newadmped0to4": [
            random.uniform(0, 10000) for _ in range(size)
        ],
        "numconfc19newadmped0to4per100k": [
            random.uniform(0, 100) for _ in range(size)
        ],
        "numconfc19newadmped0to4pctchg": [
            random.uniform(-100, 100) for _ in range(size)
        ],
        "numconfc19newadmped5to17pctchg": [
            random.uniform(-100, 100) for _ in range(size)
        ],
        "numconffluhosppatsadult": [
            random.uniform(0, 50000) for _ in range(size)
        ],
        "numconffluhosppatsped": [
            random.uniform(0, 10000) for _ in range(size)
        ],
        "numconfrsvhosppatsadult": [
            random.uniform(0, 50000) for _ in range(size)
        ],
        "numconfrsvhosppatsped": [
            random.uniform(0, 10000) for _ in range(size)
        ],
        "totalconfrsvhosppats": [
            random.uniform(0, 60000) for _ in range(size)
        ],
        "numconffluicupatsadult": [
            random.uniform(0, 10000) for _ in range(size)
        ],
        "numconffluicupatsped": [random.uniform(0, 5000) for _ in range(size)],
        "numconfrsvicupatsadult": [
            random.uniform(0, 10000) for _ in range(size)
        ],
        "numconfrsvicupatsped": [random.uniform(0, 5000) for _ in range(size)],
        "totalconfrsvicupats": [random.uniform(0, 15000) for _ in range(size)],
        "numconfc19newadmadult50to64": [
            random.uniform(0, 10000) for _ in range(size)
        ],
        "numconfc19newadmadult65to74": [
            random.uniform(0, 10000) for _ in range(size)
        ],
        "numconfc19newadmadult75plus": [
            random.uniform(0, 10000) for _ in range(size)
        ],
        "numconfflunewadmped0to4": [
            random.uniform(0, 5000) for _ in range(size)
        ],
        "numconfflunewadmped5to17": [
            random.uniform(0, 5000) for _ in range(size)
        ],
        "totalconfflunewadmped": [
            random.uniform(0, 10000) for _ in range(size)
        ],
        "numconfflunewadmadult18to49": [
            random.uniform(0, 15000) for _ in range(size)
        ],
        "numconfflunewadmadult50to64": [
            random.uniform(0, 10000) for _ in range(size)
        ],
        "numconfflunewadmadult65to74": [
            random.uniform(0, 10000) for _ in range(size)
        ],
        "numconfflunewadmadult75plus": [
            random.uniform(0, 10000) for _ in range(size)
        ],
        "totalconfflunewadmadult": [
            random.uniform(0, 30000) for _ in range(size)
        ],
        "numconfflunewadmunk": [random.uniform(0, 5000) for _ in range(size)],
        "numconfrsvnewadmped0to4": [
            random.uniform(0, 5000) for _ in range(size)
        ],
        "numconfrsvnewadmped5to17": [
            random.uniform(0, 5000) for _ in range(size)
        ],
        "totalconfrsvnewadmped": [
            random.uniform(0, 10000) for _ in range(size)
        ],
        "numconfrsvnewadmadult18to49": [
            random.uniform(0, 15000) for _ in range(size)
        ],
        "numconfrsvnewadmadult50to64": [
            random.uniform(0, 10000) for _ in range(size)
        ],
        "numconfrsvnewadmadult65to74": [
            random.uniform(0, 10000) for _ in range(size)
        ],
        "numconfrsvnewadmadult75plus": [
            random.uniform(0, 10000) for _ in range(size)
        ],
        "totalconfrsvnewadmadult": [
            random.uniform(0, 30000) for _ in range(size)
        ],
        "numconfrsvnewadmunk": [random.uniform(0, 5000) for _ in range(size)],
        "totalconfrsvnewadm": [random.uniform(0, 40000) for _ in range(size)],
        "pctconfrsvinptbeds": [random.uniform(0, 100) for _ in range(size)],
        "pctconfrsvicubeds": [random.uniform(0, 100) for _ in range(size)],
        "pctconfflunewadmadult": [random.uniform(0, 100) for _ in range(size)],
        "pctconfflunewadmped": [random.uniform(0, 100) for _ in range(size)],
        "pctconfrsvnewadmadult": [random.uniform(0, 100) for _ in range(size)],
        "pctconfrsvnewadmped": [random.uniform(0, 100) for _ in range(size)],
        "numconfc19newadmadult50to64per100k": [
            random.uniform(0, 100) for _ in range(size)
        ],
        "numconfc19newadmadult65to74per100k": [
            random.uniform(0, 100) for _ in range(size)
        ],
        "numconfc19newadmadult75plusper100k": [
            random.uniform(0, 100) for _ in range(size)
        ],
        "numconfflunewadmped0to4per100k": [
            random.uniform(0, 100) for _ in range(size)
        ],
        "numconfflunewadmped5to17per100k": [
            random.uniform(0, 100) for _ in range(size)
        ],
        "totalconfflunewadmpedper100k": [
            random.uniform(0, 100) for _ in range(size)
        ],
        "numconfflunewadmadult18to49per100k": [
            random.uniform(0, 100) for _ in range(size)
        ],
        "numconfflunewadmadult50to64per100k": [
            random.uniform(0, 100) for _ in range(size)
        ],
        "numconfflunewadmadult65to74per100k": [
            random.uniform(0, 100) for _ in range(size)
        ],
        "numconfflunewadmadult75plusper100k": [
            random.uniform(0, 100) for _ in range(size)
        ],
        "totalconfflunewadmadultper100k": [
            random.uniform(0, 100) for _ in range(size)
        ],
        "numconfrsvnewadmped0to4per100k": [
            random.uniform(0, 100) for _ in range(size)
        ],
        "numconfrsvnewadmped5to17per100k": [
            random.uniform(0, 100) for _ in range(size)
        ],
        "totalconfrsvnewadmpedper100k": [
            random.uniform(0, 100) for _ in range(size)
        ],
        "numconfrsvnewadmadult18to49per100k": [
            random.uniform(0, 100) for _ in range(size)
        ],
        "numconfrsvnewadmadult50to64per100k": [
            random.uniform(0, 100) for _ in range(size)
        ],
        "numconfrsvnewadmadult65to74per100k": [
            random.uniform(0, 100) for _ in range(size)
        ],
        "numconfrsvnewadmadult75plusper100k": [
            random.uniform(0, 100) for _ in range(size)
        ],
        "totalconfrsvnewadmadultper100k": [
            random.uniform(0, 100) for _ in range(size)
        ],
        "totalconfrsvnewadmper100k": [
            random.uniform(0, 100) for _ in range(size)
        ],
        "pctconffluinptbedsadult": [
            random.uniform(0, 100) for _ in range(size)
        ],
        "pctconffluinptbedsped": [random.uniform(0, 100) for _ in range(size)],
        "pctconffluicubedsadult": [
            random.uniform(0, 100) for _ in range(size)
        ],
        "pctconffluicubedsped": [random.uniform(0, 100) for _ in range(size)],
        "pctconfrsvinptbedsadult": [
            random.uniform(0, 100) for _ in range(size)
        ],
        "pctconfrsvinptbedsped": [random.uniform(0, 100) for _ in range(size)],
        "pctconfrsvicubedsadult": [
            random.uniform(0, 100) for _ in range(size)
        ],
        "pctconfrsvicubedsped": [random.uniform(0, 100) for _ in range(size)],
        "pctconffluhosppatsicuadult": [
            random.uniform(0, 100) for _ in range(size)
        ],
        "pctconfrsvhosppatsicu": [random.uniform(0, 100) for _ in range(size)],
        "pctconfrsvhosppatsicuadult": [
            random.uniform(0, 100) for _ in range(size)
        ],
        "pctconfrsvhosppatsicuped": [
            random.uniform(0, 100) for _ in range(size)
        ],
        "numconfc19newadmadult50to64pctchg": [
            random.uniform(-100, 100) for _ in range(size)
        ],
        "numconfc19newadmadult65to74pctchg": [
            random.uniform(-100, 100) for _ in range(size)
        ],
        "numconfc19newadmadult75pluspctchg": [
            random.uniform(-100, 100) for _ in range(size)
        ],
        "numconfflunewadmped5to17pctchg": [
            random.uniform(-100, 100) for _ in range(size)
        ],
        "totalconfflunewadmpedpctchg": [
            random.uniform(-100, 100) for _ in range(size)
        ],
        "numconfflunewadmadult18to49pctchg": [
            random.uniform(-100, 100) for _ in range(size)
        ],
        "numconfflunewadmadult50to64pctchg": [
            random.uniform(-100, 100) for _ in range(size)
        ],
        "numconfflunewadmadult65to74pctchg": [
            random.uniform(-100, 100) for _ in range(size)
        ],
        "numconfflunewadmadult75pluspctchg": [
            random.uniform(-100, 100) for _ in range(size)
        ],
        "totalconfflunewadmadultpctchg": [
            random.uniform(-100, 100) for _ in range(size)
        ],
        "numconfrsvnewadmped0to4pctchg": [
            random.uniform(-100, 100) for _ in range(size)
        ],
        "numconfrsvnewadmped5to17pctchg": [
            random.uniform(-100, 100) for _ in range(size)
        ],
        "totalconfrsvnewadmpedpctchg": [
            random.uniform(-100, 100) for _ in range(size)
        ],
        "numconfrsvnewadmadult18to49pctchg": [
            random.uniform(-100, 100) for _ in range(size)
        ],
        "numconfrsvnewadmadult50to64pctchg": [
            random.uniform(-100, 100) for _ in range(size)
        ],
        "totalconfrsvnewadmadultpctchg": [
            random.uniform(-100, 100) for _ in range(size)
        ],
        "totalconfrsvnewadmpctchg": [
            random.uniform(-100, 100) for _ in range(size)
        ],
        "numconfrsvnewadmadult75pluspctchg": [
            random.uniform(-100, 100) for _ in range(size)
        ],
        "numconfrsvnewadmadult65to74pctchg": [
            random.uniform(-100, 100) for _ in range(size)
        ],
        "pctconffluhosppatsicuped": [
            random.uniform(0, 100) for _ in range(size)
        ],
        "numconfflunewadmped0to4pctchg": [
            random.uniform(-100, 100) for _ in range(size)
        ],
    }
    df = pd.DataFrame(data)
    return df if output == "pandas" or output == "pd" else pl.from_pandas(df)
