# Smart Meter Electricity Demand Forecasting and Emissions Analysis

This repository contains the code and reproducibility notes for a machine learning class project on household electricity demand forecasting and carbon emissions analysis for London smart meter data.

The project forecasts half-hourly household electricity consumption, compares classical and neural approaches, links predicted electricity demand to UK grid carbon intensity, and evaluates policy scenarios such as cold-weather shocks, retrofits, and time-of-use flexibility.

## Sustainability Motivation

Electricity demand forecasting helps grid operators and policymakers plan for peak load, target efficiency programs, and estimate the carbon impact of demand-side interventions. This project connects household-level load forecasts to carbon intensity so that model outputs can inform practical sustainability decisions, not only prediction accuracy.

## Repository Contents

- `Colab Notebooks/Machine Learning Class Project.ipynb`  
  Main modeling notebook. It loads and cleans smart meter data, samples households, builds features, trains baselines, Ridge, LightGBM, and LSTM models, and reports evaluation results.

- `Final Code Submissions/[Code Rep]_Policy Description and Scenario Analysis for Demand.ipynb`  
  Demand-side scenario analysis using the best-performing model.

- `Final Code Submissions/Scenario Modeling and Carbon Emissions.ipynb`  
  Carbon emissions scenario analysis using demand predictions and NESO carbon intensity data.

- `Colab Notebooks/Scenario Modeling Copy.ipynb` and `Colab Notebooks/Untitled0.ipynb`  
  Supporting scenario analysis notebooks and figure/result generation.

- `Colab Notebooks/scenario_emissions_results.csv`  
  Final scenario summary used in the report.

- `Colab Notebooks/scenario_emissions_chart.png`  
  Final scenario visualization used in the report/presentation.

- `Colab Notebooks/cache/`  
  Model metadata and cached model artifacts where available. Large derived feature caches are excluded from Git and can be regenerated.

- `data/README.md`  
  Data source, expected local layout, and large-file policy.

- `docs/GOOGLE_DRIVE_DOCUMENTS.md`  
  Links to the live shared Google Docs and Slides. The Google Drive placeholder files are intentionally not tracked by Git.

- `scripts/check_project_files.py`  
  Lightweight check for expected repository files and local data availability.

## Data Sources

The project uses three linked data sources:

1. Smart Meter Energy Consumption Data in London Households  
   London Datastore: https://data.london.gov.uk/dataset/00326043-62b6-47a8-9a49-1aa226b7e2c4/

2. Weather and holiday covariates  
   Weather files are included in the London smart meter dataset structure used by the notebooks. UK bank holiday dates are stored in `Colab Notebooks/smart_meter_data/uk_bank_holidays.csv`.

3. Historic GB generation mix and carbon intensity  
   NESO Data Portal: https://www.neso.energy/data-portal/historic-generation-mix

The raw London smart meter files are large, around 10 GB unzipped in the source dataset. They are not committed directly to GitHub. See `data/README.md` for the expected folder structure.

## Setup

Python 3.10 or 3.11 is recommended.

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

On Windows PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

If running on Google Colab, install the same packages at the top of the notebook as needed.

## Reproducing Results

Place the raw and auxiliary data under the paths described in `data/README.md`, then run the notebooks in this order:

1. `Colab Notebooks/Machine Learning Class Project.ipynb`
   - Builds the cleaned feature panel from the London smart meter, weather, holiday, and household metadata files.
   - Trains and evaluates seasonal naive, Ridge, LightGBM, and LSTM models.
   - Produces the cached model files used by downstream scenario analysis.

2. `Final Code Submissions/[Code Rep]_Policy Description and Scenario Analysis for Demand.ipynb`
   - Loads the trained LightGBM model.
   - Runs demand-side counterfactual scenarios for winter 2013-2014.
   - Reports total demand, evening peak demand, and scenario deltas.

3. `Final Code Submissions/Scenario Modeling and Carbon Emissions.ipynb`
   - Merges scenario demand estimates with NESO carbon intensity.
   - Computes kgCO2 emissions by scenario.
   - Produces the emissions table used in the final report.

4. `Colab Notebooks/Untitled0.ipynb`
   - Generates `Colab Notebooks/scenario_emissions_results.csv`.
   - Generates `Colab Notebooks/scenario_emissions_chart.png`.

Before running the full notebooks, you can check whether expected files are present:

```bash
python scripts/check_project_files.py
```

## Main Results

On the common evaluation subset, LightGBM was the strongest model:

| Model | MAE | RMSE |
| --- | ---: | ---: |
| Seasonal naive | 0.1293 | 0.2724 |
| Ridge regression | 0.0870 | 0.1779 |
| LSTM | 0.0772 | 0.1735 |
| LightGBM | 0.0706 | 0.1652 |

The final scenario analysis estimated the following carbon outcomes for the winter analysis period:

| Scenario | Demand change | Peak change | Emissions change | kgCO2 saved |
| --- | ---: | ---: | ---: | ---: |
| Observed baseline | 0.00% | 0.00% | 0.00% | 0.00 |
| Cold winter -2C | +0.21% | +0.22% | +0.21% | -411.16 |
| Severe cold -3C | +0.30% | +0.33% | +0.31% | -601.01 |
| Retrofit 10% | -10.03% | -9.96% | -10.03% | 19,496.97 |
| Cold + retrofit 10% | -9.87% | -9.79% | -9.86% | 19,183.76 |
| Cold + retrofit + ToU flexibility | -10.60% | -16.10% | -10.63% | 20,653.46 |
| Strong policy package | -15.84% | -23.28% | -15.88% | 30,858.09 |

## Notes on Evaluation

This is a continuous regression task, so precision-recall curves are not applicable. The notebooks report MAE, RMSE, bias, and related diagnostics instead. For rare-event classification tasks, precision-recall would be required, but this project does not frame the problem as rare-event classification.

## Limitations

- The smart meter data covers 2011-2014 and may not represent current London demand, electrification, or tariff behavior.
- The modeling sample contains 500 stratified households rather than the full dataset.
- LightGBM has a small negative bias, which may understate demand and emissions in some periods.
- Retrofit scenarios are modeled through feature transformations rather than a physical building energy model.
- Time-of-use flexibility is modeled as a scenario overlay, not as a causal price-elasticity estimate.
- NESO carbon intensity is national/grid-level rather than London distribution-network-specific.
- The analysis does not yet include uncertainty intervals for every policy scenario.

## Large File Policy

GitHub blocks regular Git files larger than 100 MiB and recommends keeping repositories small. For that reason, raw smart meter block files and large derived feature caches are excluded from Git and documented in `data/README.md`. Model artifacts above normal Git comfort thresholds are configured for Git LFS through `.gitattributes`.

## Authors

Muhammad Ilham W, Junchi Cui, and Claire Chen.
