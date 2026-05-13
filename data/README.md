# Data Instructions

This project expects the London smart meter, weather, holiday, household metadata, and NESO carbon intensity files to be available locally in the same structure used by the notebooks.

## Expected Layout

```text
Colab Notebooks/
  neso_historic_generation_mix.csv
  smart_meter_data/
    informations_households.csv
    weather_hourly_darksky.csv
    weather_daily_darksky.csv
    uk_bank_holidays.csv
    acorn_details.csv
    darksky_parameters_documentation.html
    daily_dataset.csv
    halfhourly_dataset/
      halfhourly_dataset/
        block_0.csv
        ...
        block_111.csv
    daily_dataset/
      daily_dataset/
        block_0.csv
        ...
        block_111.csv
    hhblock_dataset/
      hhblock_dataset/
        block_0.csv
        ...
        block_111.csv
```

## Download Sources

- London smart meter dataset: https://data.london.gov.uk/dataset/00326043-62b6-47a8-9a49-1aa226b7e2c4/
- NESO historic generation mix and carbon intensity: https://www.neso.energy/data-portal/historic-generation-mix

## Why Raw Data Is Not Committed

The raw London smart meter data is large enough to make a normal GitHub repository slow and brittle. GitHub blocks regular Git files larger than 100 MiB and recommends keeping repositories small. The full source dataset is roughly 10 GB unzipped, so the reproducible approach is:

1. Keep code, notebooks, results, and documentation in GitHub.
2. Download raw data from the official source.
3. Place data in the expected paths above.
4. Regenerate derived feature caches by running the main notebook.

The following local files are intentionally excluded from Git:

- `Colab Notebooks/smart_meter_data/halfhourly_dataset/`
- `Colab Notebooks/smart_meter_data/hhblock_dataset/`
- `Colab Notebooks/smart_meter_data/daily_dataset/`
- `Colab Notebooks/smart_meter_data/daily_dataset.csv`
- `Colab Notebooks/cache/features_sample500.parquet`

Smaller metadata, weather, carbon intensity, model metadata, result tables, and charts may be tracked in the repository when size permits.
