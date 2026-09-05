CREATE TABLE dim_country (
    country_id INTEGER PRIMARY KEY,
    country_name VARCHAR(100),
    iso3 VARCHAR(3) UNIQUE,
    region VARCHAR(100)
);

CREATE TABLE dim_indicator (
    indicator_id INTEGER PRIMARY KEY,
    indicator_code VARCHAR(50),
    indicator_name VARCHAR(200),
    category VARCHAR(100),
    unit VARCHAR(50)
);

CREATE TABLE fact_economic_indicator (
    country_id INTEGER,
    indicator_id INTEGER,
    year INTEGER,
    value NUMERIC,
    source VARCHAR(100),
    data_retrieved_date DATE
);