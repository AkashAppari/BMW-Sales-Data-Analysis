"""
validate_data.py

Quick preflight checks for local data files required by notebooks.
Run: python scripts/validate_data.py
"""

import os
import sys
import pandas as pd

RAW_PATH = os.path.join("data", "raw", "BMW_Worldwide_Sales_Records_2010_2024.csv")
PROCESSED_DIR = os.path.join("data", "processed")

REQUIRED_COLUMNS = [
    "Model", "Year", "Region", "Color", "Fuel_Type", "Transmission",
    "Engine_Size_L", "Mileage_KM", "Price_USD", "Sales_Volume"
]

def main() -> int:
    ok = True

    # Check raw file exists
    if not os.path.exists(RAW_PATH):
        ok = False
        print(f"[MISSING] Raw dataset not found at: {RAW_PATH}")
        print("  Download from Kaggle and place the CSV at the above path.")
        print("  Kaggle: https://www.kaggle.com/datasets/ahmadrazakashif/bmw-worldwide-sales-records-20102024\n")
    else:
        print(f"[OK] Found raw dataset: {RAW_PATH}")
        # Spot-check required columns
        try:
            df_head = pd.read_csv(RAW_PATH, nrows=5)
            missing = [c for c in REQUIRED_COLUMNS if c not in df_head.columns]
            if missing:
                ok = False
                print(f"[WARN] Missing expected columns: {missing}")
            else:
                print("[OK] Required columns present in raw CSV (sampled).")
        except Exception as exc:
            ok = False
            print(f"[ERROR] Could not read raw CSV head: {exc}")

    # Processed directory
    if not os.path.isdir(PROCESSED_DIR):
        print(f"[INFO] Processed directory will be created by notebooks: {PROCESSED_DIR}")
    else:
        print(f"[OK] Processed directory exists: {PROCESSED_DIR}")

    print("\nSummary:")
    if ok:
        print("  ✔ Data checks passed. You can run the notebooks.")
        return 0
    else:
        print("  ✖ Some checks failed. See messages above.")
        return 1

if __name__ == "__main__":
    sys.exit(main())
