# Task 1 — Data Cleaning and Preprocessing

Internship: **Elevate Labs — Data Analyst Internship**

## Objective
Clean and prepare a raw dataset that has nulls, duplicate rows, and
inconsistent formats, using Python (Pandas).

## Files in this repo
| File | Description |
|---|---|
| `raw_sales_data.csv` | Original raw dataset (with issues) |
| `clean_data.py` | Python script that cleans the data |
| `cleaned_sales_data.csv` | Final cleaned dataset |
| `summary_of_changes.md` | Short write-up of every change made |

## Tools used
- Python
- Pandas

## What the script does
1. Loads the raw CSV
2. Renames column headers to lowercase, no spaces
3. Removes duplicate rows
4. Standardizes text values (gender, country)
5. Fills missing values (age, price → median; gender, country → "Unknown")
6. Converts all order dates to one consistent `dd-mm-yyyy` format
7. Fixes data types (age, quantity, order_id → int)
8. Saves the result as `cleaned_sales_data.csv` and prints a cleaning
   summary to the console

## How to run
```bash
pip install pandas
python clean_data.py
```

## Key learnings
- `isnull()` / `fillna()` to find and handle missing values
- `drop_duplicates()` to remove duplicate rows
- `str.lower()` / mapping dictionaries to standardize inconsistent text
- `pd.to_datetime()` to normalize mixed date formats
- `astype()` to fix column data types
