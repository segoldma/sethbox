"""
To add a daily schedule that materializes your dbt assets, uncomment the following lines.
"""
from dagster_dbt import build_schedule_from_dbt_selection

from .assets import sethbox_dbt_assets

schedules = [
    build_schedule_from_dbt_selection(
        [sethbox_dbt_assets],
        job_name="daily_dbt_models",
        cron_schedule="@daily",
        dbt_select="stg_characters",
    ),
]
