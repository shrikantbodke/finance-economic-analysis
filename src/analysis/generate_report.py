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

# Economic insight: highest GDP growth
highest_gdp_growth = summary.loc[summary["GDP_GROWTH"].idxmax()]

print("\nEconomic Insights")
print("-----------------")

print(
    "Highest GDP Growth:",
    highest_gdp_growth["country"],
    "-",
    round(highest_gdp_growth["GDP_GROWTH"], 2),
    "%"
)

# Economic insight: lowest GDP growth
lowest_gdp_growth = summary.loc[summary["GDP_GROWTH"].idxmin()]

print(
    "Lowest GDP Growth:",
    lowest_gdp_growth["country"],
    "-",
    round(lowest_gdp_growth["GDP_GROWTH"], 2),
    "%"
)
# Economic insight: highest inflation
highest_inflation = summary.loc[summary["INFLATION"].idxmax()]

print(
    "Highest Inflation:",
    highest_inflation["country"],
    "-",
    round(highest_inflation["INFLATION"], 2),
    "%"
)
# Economic insight: highest unemployment
highest_unemployment = summary.loc[summary["UNEMPLOYMENT"].idxmax()]

print(
    "Highest Unemployment:",
    highest_unemployment["country"],
    "-",
    round(highest_unemployment["UNEMPLOYMENT"], 2),
    "%"
)
# Economic insight: highest GDP per capita
highest_gdp_pc = summary.loc[summary["GDP_PC"].idxmax()]

print(
    "Highest GDP per Capita:",
    highest_gdp_pc["country"],
    "-",
    round(highest_gdp_pc["GDP_PC"], 2),
    "USD"
)

# Economic insight: highest FDI
highest_fdi = summary.loc[summary["FDI"].idxmax()]

print(
    "Highest FDI:",
    highest_fdi["country"],
    "-",
    round(highest_fdi["FDI"], 2),
    "USD"
)

print(
    "Highest FDI:",
    highest_fdi["country"],
    "-",
    round(highest_fdi["FDI"], 2),
    "USD"
)

# Economic insight: highest exports
highest_exports = summary.loc[summary["EXPORTS"].idxmax()]

print(
    "Highest Exports:",
    highest_exports["country"],
    "-",
    round(highest_exports["EXPORTS"], 2),
    "USD"
)

# Economic insight: highest imports
highest_imports = summary.loc[summary["IMPORTS"].idxmax()]

print(
    "Highest Imports:",
    highest_imports["country"],
    "-",
    round(highest_imports["IMPORTS"], 2),
    "USD"
)

# Economic insight: highest current account balance
highest_current_account = summary.loc[summary["CURRENT_ACCOUNT"].idxmax()]

print(
    "Highest Current Account Balance:",
    highest_current_account["country"],
    "-",
    round(highest_current_account["CURRENT_ACCOUNT"], 2),
    "% GDP"
)

# Economic insight: lowest current account balance
lowest_current_account = summary.loc[summary["CURRENT_ACCOUNT"].idxmin()]

print(
    "Lowest Current Account Balance:",
    lowest_current_account["country"],
    "-",
    round(lowest_current_account["CURRENT_ACCOUNT"], 2),
    "% GDP"
)

# Economic insight: highest population
highest_population = summary.loc[summary["POPULATION"].idxmax()]

print(
    "Highest Population:",
    highest_population["country"],
    "-",
    round(highest_population["POPULATION"], 0),
    "people"
)

# Economic insight: average GDP growth
average_gdp_growth = summary["GDP_GROWTH"].mean()

print(
    "Average GDP Growth:",
    round(average_gdp_growth, 2),
    "%"
)

# Economic insight: average inflation
average_inflation = summary["INFLATION"].mean()

print(
    "Average Inflation:",
    round(average_inflation, 2),
    "%"
)

# Economic insight: average unemployment
average_unemployment = summary["UNEMPLOYMENT"].mean()

print(
    "Average Unemployment:",
    round(average_unemployment, 2),
    "%"
)

# Economic insight: average GDP per capita
average_gdp_pc = summary["GDP_PC"].mean()

print(
    "Average GDP per Capita:",
    round(average_gdp_pc, 2),
    "USD"
)

# Economic insight: average FDI
average_fdi = summary["FDI"].mean()

print(
    "Average FDI:",
    round(average_fdi, 2),
    "USD"
)

# Economic insight: average exports
average_exports = summary["EXPORTS"].mean()

print(
    "Average Exports:",
    round(average_exports, 2),
    "USD"
)

# Economic insight: average imports
average_imports = summary["IMPORTS"].mean()

print(
    "Average Imports:",
    round(average_imports, 2),
    "USD"
)

# Economic insight: average current account balance
average_current_account = summary["CURRENT_ACCOUNT"].mean()

print(
    "Average Current Account Balance:",
    round(average_current_account, 2),
    "% GDP"
)

# Economic insight: average population
average_population = summary["POPULATION"].mean()

print(
    "Average Population:",
    round(average_population, 0),
    "people"
)