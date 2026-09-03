import pandas as pd

# Load processed data
input_file = "data/processed/economic_indicators_clean.csv"

df = pd.read_csv(input_file)

print("Economic Analysis Dataset")
print("-------------------------")

print("Rows:", len(df))
print("Countries:", df["countryiso3code"].nunique())
print("Indicators:", df["indicator"].nunique())

# Create a 2024 analysis dataset
df_2024 = df[df["date"] == 2024].copy()

print("\n2024 Analysis Dataset")
print("--------------------")
print("Rows:", len(df_2024))

print("\nCountries:")
print(df_2024["country"].unique())

print("\nIndicators:")
print(df_2024["indicator"].unique())

# Save analysis dataset
output_file = "data/final/economic_analysis_2024.csv"

df_2024.to_csv(output_file, index=False)

print("\nAnalysis dataset saved to:", output_file)