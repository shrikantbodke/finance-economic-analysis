import pandas as pd
from sqlalchemy import create_engine

# PostgreSQL connection
DB_PASSWORD = "Gurudev%401234"

engine = create_engine(
    f"postgresql+psycopg2://postgres:{DB_PASSWORD}@localhost:5432/west_africa_economic"
)

# Load cleaned economic data
df = pd.read_csv(
    "data/processed/economic_indicators_clean.csv"
)

# Create country dimension
countries = df[
    ["countryiso3code", "country"]
].drop_duplicates().reset_index(drop=True)

countries["country_id"] = range(1, len(countries) + 1)
countries["region"] = "West Africa"

countries = countries[
    ["country_id", "country", "countryiso3code", "region"]
]

countries.columns = [
    "country_id",
    "country_name",
    "iso3",
    "region"
]

# Create indicator dimension
indicator_names = {
    "GDP_GROWTH": "GDP growth",
    "GDP_PC": "GDP per capita",
    "INFLATION": "Inflation",
    "UNEMPLOYMENT": "Unemployment",
    "GOV_DEBT": "Government debt",
    "FDI": "Foreign direct investment",
    "EXPORTS": "Exports",
    "IMPORTS": "Imports",
    "CURRENT_ACCOUNT": "Current account balance",
    "POPULATION": "Population"
}

indicator_categories = {
    "GDP_GROWTH": "Growth",
    "GDP_PC": "Growth",
    "INFLATION": "Monetary",
    "UNEMPLOYMENT": "Labor",
    "GOV_DEBT": "Fiscal",
    "FDI": "Investment",
    "EXPORTS": "Trade",
    "IMPORTS": "Trade",
    "CURRENT_ACCOUNT": "External",
    "POPULATION": "Demographics"
}

indicator_units = {
    "GDP_GROWTH": "%",
    "GDP_PC": "USD",
    "INFLATION": "%",
    "UNEMPLOYMENT": "%",
    "GOV_DEBT": "% GDP",
    "FDI": "USD",
    "EXPORTS": "USD",
    "IMPORTS": "USD",
    "CURRENT_ACCOUNT": "% GDP",
    "POPULATION": "Number"
}

indicators = pd.DataFrame({
    "indicator_code": sorted(df["indicator"].unique())
})

indicators["indicator_id"] = range(1, len(indicators) + 1)

indicators["indicator_name"] = indicators["indicator_code"].map(
    indicator_names
)

indicators["category"] = indicators["indicator_code"].map(
    indicator_categories
)

indicators["unit"] = indicators["indicator_code"].map(
    indicator_units
)

indicators = indicators[
    [
        "indicator_id",
        "indicator_code",
        "indicator_name",
        "category",
        "unit"
    ]
]

# Create fact table
fact = df.merge(
    countries[["country_id", "iso3"]],
    left_on="countryiso3code",
    right_on="iso3",
    how="left"
)

fact = fact.merge(
    indicators[["indicator_id", "indicator_code"]],
    left_on="indicator",
    right_on="indicator_code",
    how="left"
)

fact["year"] = fact["date"].astype(int)

fact["source"] = "World Bank"

fact["data_retrieved_date"] = pd.Timestamp.today().date()

fact = fact[
    [
        "country_id",
        "indicator_id",
        "year",
        "value",
        "source",
        "data_retrieved_date"
    ]
]

# Load dimensions and fact table
countries.to_sql(
    "dim_country",
    engine,
    if_exists="append",
    index=False
)

indicators.to_sql(
    "dim_indicator",
    engine,
    if_exists="append",
    index=False
)

fact.to_sql(
    "fact_economic_indicator",
    engine,
    if_exists="append",
    index=False
)

print("PostgreSQL database loading completed successfully.")
print("Countries loaded:", len(countries))
print("Indicators loaded:", len(indicators))
print("Economic records loaded:", len(fact))