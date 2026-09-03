import requests


def fetch_world_bank_data(country_code, indicator_code, start_year, end_year):
    url = (
        f"https://api.worldbank.org/v2/country/{country_code}/indicator/"
        f"{indicator_code}?date={start_year}:{end_year}&format=json&per_page=100"
    )

    response = requests.get(url, timeout=90)
    response.raise_for_status()

    return response.json()

if __name__ == "__main__":
    data = fetch_world_bank_data(
        "BEN",
        "NY.GDP.MKTP.KD.ZG",
        2020,
        2024,
    )

    print(data[1][0])