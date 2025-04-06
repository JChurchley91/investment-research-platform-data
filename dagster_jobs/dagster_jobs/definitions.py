from dagster import Definitions, load_assets_from_modules

import dagster_jobs.assets as assets

all_assets = load_assets_from_modules([assets])

defs = Definitions(
    assets=all_assets,
)
