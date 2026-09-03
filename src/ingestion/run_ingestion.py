from world_bank_api import fetch_world_bank_data


COUNTRIES = [
    "BEN",
    "BFA",
    "CIV",
    "GHA",
    "GIN",
    "LBR",
    "MLI",
    "SEN",
    "SLE",
]

INDICATORS = [
    "NY.GDP.MKTP.KD.ZG",
    "NY.GDP.PCAP.CD",
    "FP.CPI.TOTL.ZG",
    "SL.UEM.TOTL.ZS",
    "GC.DOD.TOTL.GD.ZS",
    "BX.KLT.DINV.CD.WD",
    "NE.EXP.GNFS.CD",
    "NE.IMP.GNFS.CD",
    "BN.CAB.XOKA.GD.ZS",
    "SP.POP.TOTL",
]

all_records = []


for country in COUNTRIES:
    for indicator in INDICATORS:
        print(f"Fetching {indicator} for {country}")

        data = fetch_world_bank_data(
            country,
            indicator,
            2020,
            2024,
        )

        all_records.extend(data[1])

        print(f"Records returned: {len(data[1])}")

import csv

output_file = "data/raw/economic_indicators.csv"

with open(output_file, "w", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(
        file,
        fieldnames=[
            "countryiso3code",
            "country",
            "indicator",
            "date",
            "value"
        ]
    )

    writer.writeheader()

    for record in all_records:
        writer.writerow({
            "countryiso3code": record.get("countryiso3code"),
            "country": record.get("country", {}).get("value"),
            "indicator": record.get("indicator", {}).get("id"),
            "date": record.get("date"),
            "value": record.get("value")
        })

print(f"Raw data saved to {output_file}")