import pandas as pd

from world_bank_api import fetch_world_bank_data


# Countries defined in dim_country.csv
countries = [
    "BEN",
    "BFA",
    "CIV",
    "GHA",
    "GIN",
    "LBR",
    "MLI",
    "SEN",
    "SLE"
]


# Indicators mapped to World Bank API codes
indicators = {
    "GDP_GROWTH": "NY.GDP.MKTP.KD.ZG",
    "GDP_PC": "NY.GDP.PCAP.CD",
    "INFLATION": "FP.CPI.TOTL.ZG",
    "UNEMPLOYMENT": "SL.UEM.TOTL.ZS",
    "GOV_DEBT": "GC.DOD.TOTL.GD.ZS",
    "FDI": "BX.KLT.DINV.CD.WD",
    "EXPORTS": "NE.EXP.GNFS.CD",
    "IMPORTS": "NE.IMP.GNFS.CD",
    "CURRENT_ACCOUNT": "BN.CAB.XOKA.GD.ZS",
    "POPULATION": "SP.POP.TOTL"
}


start_year = 2020
end_year = 2024


records = []


for country in countries:

    for indicator_code, world_bank_code in indicators.items():

        print(
            f"Fetching {indicator_code} "
            f"for {country}..."
        )

        data = fetch_world_bank_data(
            country,
            world_bank_code,
            start_year,
            end_year
        )

        # World Bank response structure:
        # [metadata, data_records]

        if len(data) < 2:
            continue

        for row in data[1]:

            records.append({
                "country_code": country,
                "indicator_code": indicator_code,
                "year": int(row["date"]),
                "value": row["value"]
            })


# Convert collected records into DataFrame
df = pd.DataFrame(records)


# Save raw World Bank data
output_file = "data/raw/world_bank_economic_data.csv"

df.to_csv(
    output_file,
    index=False
)


print()
print("World Bank ingestion completed.")
print("Rows collected:", len(df))
print("Output file:", output_file)