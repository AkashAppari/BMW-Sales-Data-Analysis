"""
data_cleaning.py

Utility functions for cleaning and inspecting the BMW Worldwide Sales dataset.
Used in notebooks/01_data_cleaning.ipynb.
"""

import pandas as pd
import os
from typing import Optional


class DataCleaningError(Exception):
    """Custom exception for data cleaning operations."""
    pass


def load_data(file_path: str) -> pd.DataFrame:
    """Load CSV dataset into a pandas DataFrame.

    Raises DataCleaningError if the file is missing or cannot be read.
    """
    print(f"Loading dataset from: {file_path}")
    if not os.path.exists(file_path):
        raise DataCleaningError(f"File not found: {file_path}")

    try:
        df = pd.read_csv(file_path)
    except Exception as exc:
        raise DataCleaningError(f"Failed to read CSV: {file_path}; {exc}")

    if df.empty:
        raise DataCleaningError(f"Loaded dataframe is empty: {file_path}")

    print(f"Loaded dataset with {df.shape[0]} rows and {df.shape[1]} columns.")
    return df


def inspect_data(df: pd.DataFrame) -> None:
    """Print data shape, column types, and missing value summary."""
    if df is None or not isinstance(df, pd.DataFrame):
        raise DataCleaningError("inspect_data expects a pandas DataFrame")

    print("\n--- Data Overview ---")
    print(f"Shape: {df.shape}")
    print("\nData types:")
    print(df.dtypes)
    print("\nFirst five rows:")
    print(df.head())

    missing = df.isna().sum()
    missing_percent = (missing / len(df)) * 100 if len(df) > 0 else missing * 0
    summary = pd.DataFrame(
        {"Missing_Count": missing, "Missing_Percent": missing_percent.round(2)}
    )
    print("\nMissing values per column:")
    print(summary[summary["Missing_Count"] > 0] if summary["Missing_Count"].sum() > 0 else "No missing values found.")


def remove_duplicates(df: pd.DataFrame) -> pd.DataFrame:
    """Remove duplicate rows from DataFrame."""
    if df is None or not isinstance(df, pd.DataFrame):
        raise DataCleaningError("remove_duplicates expects a pandas DataFrame")

    duplicates = int(df.duplicated().sum())
    print(f"\nDuplicate rows found: {duplicates}")
    if duplicates > 0:
        df = df.drop_duplicates()
        print(f"Removed duplicates. New shape: {df.shape}")
    else:
        print("No duplicates found.")
    return df


def fill_missing_values(df: pd.DataFrame) -> pd.DataFrame:
    """
    Fill missing values:
      - Numeric columns: fill with median
      - Object (categorical) columns: fill with mode
    """
    df = df.copy()
    if df.empty:
        print("Warning: fill_missing_values received an empty DataFrame")
        return df

    num_cols = df.select_dtypes(include=["number"]).columns.tolist()
    obj_cols = df.select_dtypes(include=["object", "category"]).columns.tolist()

    for col in num_cols:
        try:
            median_val = df[col].median()
            if pd.isna(median_val):
                # skip columns that are all NaN
                continue
            df[col].fillna(median_val, inplace=True)
        except Exception:
            # If a numeric operation fails, continue with other columns
            print(f"Warning: could not fill numeric column: {col}")

    for col in obj_cols:
        try:
            mode_val = df[col].mode(dropna=True)
            if not mode_val.empty:
                df[col].fillna(mode_val[0], inplace=True)
        except Exception:
            print(f"Warning: could not fill categorical column: {col}")

    print("Filled missing values using median (numeric) and mode (categorical) where applicable.")
    return df


def summarize_data(df: pd.DataFrame) -> None:
    """Print summary statistics for numeric and categorical columns."""
    if df is None or not isinstance(df, pd.DataFrame):
        raise DataCleaningError("summarize_data expects a pandas DataFrame")

    print("\n--- Numeric Columns Summary ---")
    try:
        print(df.describe().transpose())
    except Exception as exc:
        print(f"Warning: failed to describe numeric columns: {exc}")

    print("\n--- Categorical Columns Summary (Top 5 values) ---")
    for col in df.select_dtypes(include=["object", "category"]).columns:
        print(f"\nColumn: {col}")
        try:
            print(df[col].value_counts().head())
        except Exception:
            print(f"  (could not compute value counts for {col})")


def clean_dataset(raw_path: str, save_path: str) -> pd.DataFrame:
    """
    End-to-end cleaning pipeline:
      1. Load data
      2. Inspect data
      3. Remove duplicates
      4. Fill missing values
      5. Save cleaned dataset
    """
    try:
        df = load_data(raw_path)
        inspect_data(df)
        df = remove_duplicates(df)
        df = fill_missing_values(df)

        os.makedirs(os.path.dirname(save_path), exist_ok=True)
        df.to_csv(save_path, index=False)
        print(f"\nCleaned dataset saved to: {save_path}")
        return df
    except DataCleaningError:
        # Re-raise known data cleaning errors
        raise
    except Exception as exc:
        raise DataCleaningError(f"Failed to clean dataset: {exc}")
