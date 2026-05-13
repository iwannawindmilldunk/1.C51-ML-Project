from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

REQUIRED_CODE_FILES = [
    "Colab Notebooks/Machine Learning Class Project.ipynb",
    "Final Code Submissions/[Code Rep]_Policy Description and Scenario Analysis for Demand.ipynb",
    "Final Code Submissions/Scenario Modeling and Carbon Emissions.ipynb",
    "Colab Notebooks/scenario_emissions_results.csv",
    "Colab Notebooks/scenario_emissions_chart.png",
    "Colab Notebooks/neso_historic_generation_mix.csv",
    "Colab Notebooks/smart_meter_data/informations_households.csv",
    "Colab Notebooks/smart_meter_data/weather_hourly_darksky.csv",
    "Colab Notebooks/smart_meter_data/weather_daily_darksky.csv",
    "Colab Notebooks/smart_meter_data/uk_bank_holidays.csv",
    "Colab Notebooks/smart_meter_data/acorn_details.csv",
]

LARGE_LOCAL_DATA = [
    "Colab Notebooks/smart_meter_data/halfhourly_dataset/halfhourly_dataset/block_0.csv",
    "Colab Notebooks/smart_meter_data/daily_dataset/daily_dataset/block_0.csv",
    "Colab Notebooks/smart_meter_data/hhblock_dataset/hhblock_dataset/block_0.csv",
    "Colab Notebooks/smart_meter_data/daily_dataset.csv",
]


def report(paths: list[str], label: str) -> bool:
    print(f"\n{label}")
    print("-" * len(label))
    missing = []
    for rel_path in paths:
        path = ROOT / rel_path
        status = "ok" if path.exists() else "missing"
        print(f"{status:8} {rel_path}")
        if not path.exists():
            missing.append(rel_path)
    return not missing


def main() -> int:
    code_ok = report(REQUIRED_CODE_FILES, "Required code/result files")
    data_ok = report(LARGE_LOCAL_DATA, "Large local data files")

    print("\nSummary")
    print("-------")
    if code_ok:
        print("Repository files needed for review are present.")
    else:
        print("Some tracked code/result files are missing.")

    if data_ok:
        print("Large local data files are available for full notebook reruns.")
    else:
        print("Large local data files are absent or intentionally not tracked; see data/README.md.")

    return 0 if code_ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
