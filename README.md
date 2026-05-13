# Smart Meter Electricity Demand Forecasting and Emissions Analysis

This repository contains the clean, runnable code submission for a machine learning class project on London household electricity demand forecasting and carbon emissions analysis.

The project forecasts half-hourly smart meter electricity consumption, compares classical and neural models, links demand to UK grid carbon intensity, and evaluates sustainability scenarios including cold-weather stress, retrofits, and time-of-use flexibility.

## Repository Structure

```text
.
|-- notebooks/
|   |-- 01_model_training.ipynb
|   |-- 02_demand_policy_scenarios.ipynb
|   |-- 03_carbon_emissions_analysis.ipynb
|   |-- executed/
|   `-- archive/
|-- data/
|   |-- README.md
|   |-- carbon/
|   `-- metadata/
|-- models/
|-- results/
|-- docs/
|-- scripts/
|-- requirements.txt
`-- README.md
```

## Main Notebooks

- `notebooks/01_model_training.ipynb`  
  Cleans and samples the smart meter data, merges weather/holiday/household covariates, builds the feature panel, and trains the seasonal naive, Ridge, LightGBM, and LSTM models.

- `notebooks/02_demand_policy_scenarios.ipynb`  
  Uses the trained LightGBM model to evaluate demand-side counterfactual scenarios.

- `notebooks/03_carbon_emissions_analysis.ipynb`  
  Combines scenario demand predictions with NESO carbon intensity to estimate emissions impacts.

- `notebooks/archive/`  
  Earlier supporting notebooks kept for traceability, not the primary execution path.

- `notebooks/executed/`  
  Executed snapshots copied from the original project workspace. These preserve intermediate outputs, plots, and tables for visual review.

- `results/notebook_figures/`  
  Extracted PNG figures from the executed notebooks for quick browsing.

## Data

Tracked data files are limited to small metadata, weather, results, and the NESO carbon-intensity CSV. Full raw smart meter block data is intentionally not committed because the unzipped dataset is roughly 10 GB.

Expected raw data location for full reruns:

```text
data/raw/smart_meter_data/
```

See `data/README.md` for download sources and exact expected layout.

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

## Reproducing Results

Run notebooks in this order:

1. `notebooks/01_model_training.ipynb`
   - Generates `data/processed/features_sample500.parquet`
   - Saves model artifacts to `models/`

2. `notebooks/02_demand_policy_scenarios.ipynb`
   - Saves policy scenario summary tables to `results/`

3. `notebooks/03_carbon_emissions_analysis.ipynb`
   - Saves emissions scenario outputs to `results/`

Before a full run, check the repository layout:

```bash
python scripts/check_project_files.py
```

For review without rerunning the full 10 GB pipeline, open the notebooks in `notebooks/executed/` or browse `results/notebook_figures/`.

## Main Results

LightGBM was the strongest model on the common evaluation subset.

| Model | MAE | RMSE |
| --- | ---: | ---: |
| Seasonal naive | 0.1293 | 0.2724 |
| Ridge regression | 0.0870 | 0.1779 |
| LSTM | 0.0772 | 0.1735 |
| LightGBM | 0.0706 | 0.1652 |

Final winter scenario results:

| Scenario | Demand change | Peak change | Emissions change | kgCO2 saved |
| --- | ---: | ---: | ---: | ---: |
| Observed baseline | 0.00% | 0.00% | 0.00% | 0.00 |
| Cold winter -2C | +0.21% | +0.22% | +0.21% | -411.16 |
| Severe cold -3C | +0.30% | +0.33% | +0.31% | -601.01 |
| Retrofit 10% | -10.03% | -9.96% | -10.03% | 19,496.97 |
| Cold + retrofit 10% | -9.87% | -9.79% | -9.86% | 19,183.76 |
| Cold + retrofit + ToU flexibility | -10.60% | -16.10% | -10.63% | 20,653.46 |
| Strong policy package | -15.84% | -23.28% | -15.88% | 30,858.09 |

## Evaluation Note

This is a continuous regression task, so precision-recall curves are not applicable. The project reports MAE, RMSE, bias, and scenario-level emissions diagnostics. Precision-recall would be required for rare-event classification tasks, but that is not the formulation used here.

## Limitations

- The smart meter data covers 2011-2014 and may not represent current London demand, electrification, or tariff behavior.
- The modeling sample uses 500 stratified households rather than the full dataset.
- LightGBM has a small negative bias, which may understate demand and emissions in some periods.
- Retrofit scenarios use feature transformations rather than a physical building energy model.
- Time-of-use flexibility is a scenario overlay, not a causal price-elasticity estimate.
- NESO carbon intensity is national/grid-level rather than London distribution-network-specific.
- The analysis does not yet include uncertainty intervals for every policy scenario.

## Authors

Muhammad Ilham W, Junchi Cui, and Claire Chen.
