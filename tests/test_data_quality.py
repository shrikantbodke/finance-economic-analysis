import pandas as pd

# Load processed data
file_path = "data/processed/economic_indicators_clean.csv"

df = pd.read_csv(file_path)

print("Data Quality Validation")
print("-----------------------")

# 1. Check row count
print("Rows:", len(df))

# 2. Check columns
print("Columns:", list(df.columns))

# 3. Check missing values
print("\nMissing values:")
print(df.isna().sum())

# 4. Check duplicate records
print("\nDuplicate rows:", df.duplicated().sum())

# 5. Check countries
print("\nCountries:", df["countryiso3code"].nunique())

# 6. Check indicators
print("Indicators:", df["indicator"].nunique())

# 7. Check years
print("Years:", sorted(df["date"].unique()))

# 8. Validation checks
assert len(df) > 0
assert df["countryiso3code"].notna().all()
assert df["indicator"].notna().all()
assert df["date"].notna().all()
assert df["value"].notna().all()
assert df.duplicated().sum() == 0

print("\nAll data quality checks passed.")