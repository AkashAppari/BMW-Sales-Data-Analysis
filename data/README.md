# Data Guide

This project does not commit large CSVs to the repository to keep it lightweight. Follow these steps to run the notebooks end-to-end.

## Download
- Source (Kaggle): https://www.kaggle.com/datasets/ahmadrazakashif/bmw-worldwide-sales-records-20102024
- Download the file: `BMW_Worldwide_Sales_Records_2010_2024.csv`

## Place files
- Put the downloaded file here:
  - `data/raw/BMW_Worldwide_Sales_Records_2010_2024.csv`
- The cleaning and feature engineering notebooks will generate processed files here:
  - `data/processed/BMW_Worldwide_Sales_Cleaned.csv`
  - `data/processed/BMW_Worldwide_Sales_Features.csv`

## Notes
- Raw and processed CSVs are intentionally gitignored.
- If the raw CSV is missing, notebooks will error on load. Run `scripts/validate_data.py` (added in this repo) for a quick preflight check.
