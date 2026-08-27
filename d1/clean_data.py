"""
Task 1: Data Cleaning and Preprocessing
Cleans raw_sales_data.csv and saves cleaned_sales_data.csv
"""

import pandas as pd

# ---- 1. Load raw data ----
df = pd.read_csv("raw_sales_data.csv")
rows_before = len(df)

# ---- 2. Clean column headers: lowercase, no spaces ----
df.columns = [c.strip().lower().replace(" ", "_") for c in df.columns]

# ---- 3. Remove duplicate rows ----
dup_count = df.duplicated().sum()
df = df.drop_duplicates()

# ---- 4. Standardize text values ----
# gender: map many spellings to Male / Female
gender_map = {
    "male": "Male", "m": "Male",
    "female": "Female", "f": "Female"
}
df["gender"] = df["gender"].str.strip().str.lower().map(gender_map)

# country: fix casing / abbreviations
country_map = {
    "india": "India", "bharat": "India",
    "usa": "USA", "u.s.a": "USA", "united states": "USA",
    "uk": "UK", "u.k": "UK", "united kingdom": "UK",
    "australia": "Australia", "aus": "Australia"
}
df["country"] = df["country"].str.strip().str.lower().map(country_map)

# ---- 5. Fix missing values ----
missing_before = df.isnull().sum()

# age: fill with median age, then convert to int
df["age"] = df["age"].fillna(df["age"].median()).astype(int)

# price: fill with median price
df["price"] = df["price"].fillna(df["price"].median()).round(2)

# gender/country: too few clues to guess, so mark as "Unknown"
df["gender"] = df["gender"].fillna("Unknown")
df["country"] = df["country"].fillna("Unknown")

missing_after = df.isnull().sum()

# ---- 6. Convert dates to one consistent format (dd-mm-yyyy) ----
df["order_date"] = pd.to_datetime(df["order_date"], format="mixed", dayfirst=True)
df["order_date"] = df["order_date"].dt.strftime("%d-%m-%Y")

# ---- 7. Fix data types ----
df["order_id"] = df["order_id"].astype(int)
df["quantity"] = df["quantity"].astype(int)

# ---- 8. Save cleaned data ----
df.to_csv("cleaned_sales_data.csv", index=False)
rows_after = len(df)

# ---- 9. Print a short summary of changes ----
print("CLEANING SUMMARY")
print("-" * 40)
print(f"Rows before cleaning : {rows_before}")
print(f"Duplicate rows removed: {dup_count}")
print(f"Rows after cleaning  : {rows_after}")
print()
print("Missing values before cleaning:")
print(missing_before[missing_before > 0])
print()
print("Missing values after cleaning:")
print(missing_after)
print()
print("Column headers renamed to lowercase_with_underscores.")
print("Gender and Country text values standardized.")
print("Order dates converted to a single dd-mm-yyyy format.")
print("Age, Quantity, Order ID converted to whole numbers (int).")
