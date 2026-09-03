import pandas as pd


input_file = "data/raw/economic_indicators.csv"

df = pd.read_csv(input_file)

# Convert date to integer
df["date"] = pd.to_numeric(df["date"], errors="coerce")

# Convert value to numeric
df["value"] = pd.to_numeric(df["value"], errors="coerce")

# Remove duplicate records
df = df.drop_duplicates()

# Sort data
df = df.sort_values(
    by=["countryiso3code", "indicator", "date"]
)

# Reset index
df = df.reset_index(drop=True)

print("Cleaned Rows:", len(df))
print("Columns:", len(df.columns))
print("\nMissing values:")
print(df.isna().sum())

print("\nCleaned data:")
print(df.head())

# Remove records with missing economic values
df = df.dropna(subset=["value"])

print("\nRows after removing missing values:", len(df))
print("Remaining missing values:")
print(df.isna().sum())

# Save processed data
output_file = "data/processed/economic_indicators_clean.csv"


# Standardize World Bank indicator codes
indicator_mapping = {
    "NY.GDP.MKTP.KD.ZG": "GDP_GROWTH",
    "NY.GDP.PCAP.CD": "GDP_PC",
    "FP.CPI.TOTL.ZG": "INFLATION",
    "SL.UEM.TOTL.ZS": "UNEMPLOYMENT",
    "GC.DOD.TOTL.GD.ZS": "GOV_DEBT",
    "BX.KLT.DINV.CD.WD": "FDI",
    "NE.EXP.GNFS.CD": "EXPORTS",
    "NE.IMP.GNFS.CD": "IMPORTS",
    "BN.CAB.XOKA.GD.ZS": "CURRENT_ACCOUNT",
    "SP.POP.TOTL": "POPULATION"
}

df["indicator"] = df["indicator"].map(indicator_mapping)

print("\nStandardized indicators:")
print(df["indicator"].value_counts())

# Save final processed data
df.to_csv(output_file, index=False)

print("\nFinal processed data saved to:", output_file)