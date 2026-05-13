# Notebook Execution Order

Run the notebooks from the repository root in this order:

1. `01_model_training.ipynb`
   - Builds the cleaned feature panel.
   - Trains baseline, Ridge, LightGBM, and LSTM models.
   - Writes derived features to `data/processed/`.
   - Writes trained model artifacts to `models/`.

2. `02_demand_policy_scenarios.ipynb`
   - Loads the LightGBM model and processed features.
   - Evaluates demand-side policy scenarios.
   - Writes scenario summaries to `results/`.

3. `03_carbon_emissions_analysis.ipynb`
   - Loads scenario predictions and NESO carbon intensity data.
   - Computes carbon emissions impacts.
   - Writes final emissions outputs to `results/`.

The `archive/` folder keeps earlier exploratory notebooks for traceability. The three numbered notebooks are the clean execution path for review.

The `executed/` folder keeps rendered snapshots from the original workspace, including intermediate outputs, tables, and plots. Use these when you want to inspect the analysis without rerunning the full raw-data pipeline.
