from datetime import datetime
from io import BytesIO

import polars as pl

from cfa.dataops import datacat

dataset = datacat.public.mcmv.nis


def get_date() -> str:
    return datetime.now().strftime("%Y-%m-%dT%H:%M:%S")


def load() -> None:
    # get datasets
    flu_vax_weekly_c = (
        datacat.public.mcmv.flu_vax_weekly_cumulative.load.get_dataframe(
            "pl_lazy"
        )
    )
    flu_vax_weekly = datacat.public.mcmv.flu_vax_weekly.load.get_dataframe(
        "pl_lazy"
    )
    covid_survey_resp_vax_view = (
        datacat.public.mcmv.covid_survey_resp_vax_view.load.get_dataframe(
            "pl_lazy"
        )
    )
    parental_vax_intent_weekly = (
        datacat.public.mcmv.parental_vax_intent_weekly.load.get_dataframe(
            "pl_lazy"
        )
    )
    covid_survey_trends_and_intent = (
        datacat.public.mcmv.covid_survey_trends_and_intent.load.get_dataframe(
            "pl_lazy"
        )
    )
    rsv_infant_protection = (
        datacat.public.mcmv.rsv_infant_protection.load.get_dataframe("pl_lazy")
    )
    covid_vax_weekly_c = (
        datacat.public.mcmv.covid_vax_weekly_cumulative.load.get_dataframe(
            "pl_lazy"
        )
    )
    rsv_vax_weekly_c = (
        datacat.public.mcmv.rsv_vax_weekly_cumulative.load.get_dataframe(
            "pl_lazy"
        )
    )
    flu_vax_all_ages = datacat.public.mcmv.flu_vax_all_ages.load.get_dataframe(
        "pl_lazy"
    )

    # combine datasets
    df = pl.concat(
        [
            flu_vax_weekly_c,
            flu_vax_weekly,
            covid_survey_resp_vax_view,
            parental_vax_intent_weekly,
            covid_survey_trends_and_intent,
            rsv_infant_protection,
            covid_vax_weekly_c,
            rsv_vax_weekly_c,
            flu_vax_all_ages,
        ],
        how="vertical_relaxed",
    ).collect()

    # write to load
    buffer = BytesIO()
    df.write_parquet(buffer)
    updated_date = get_date()
    dataset.load.write_blob(
        file_buffer=buffer.getvalue(),
        path_after_prefix=f"{updated_date}/data.parquet",
        auto_version=False,
    )
    buffer.close()
