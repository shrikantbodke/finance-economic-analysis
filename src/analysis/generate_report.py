import pandas as pd

# Load the 2024 analysis dataset
input_file = "data/final/economic_analysis_2024.csv"

df = pd.read_csv(input_file)

print("Economic Report Generation")
print("--------------------------")

print("\nTotal rows:", len(df))
print("Countries:", df["country"].nunique())
print("Indicators:", df["indicator"].nunique())

# Create country-level summary
summary = df.pivot(
    index="country",
    columns="indicator",
    values="value"
).reset_index()

print("\nCountry Economic Summary")
print("------------------------")
print(summary)

# Save country summary
output_file = "reports/country_economic_summary_2024.csv"

summary.to_csv(output_file, index=False)

print("\nReport saved to:", output_file)