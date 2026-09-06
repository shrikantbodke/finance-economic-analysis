SELECT
    c.country_name,
    f.year,
    f.value
FROM fact_economic_indicator f
JOIN dim_country c
ON f.country_id = c.country_id
WHERE f.indicator_id = 1
AND f.year = 2024;


SELECT
    c.country_name,
    f.value AS gdp_growth
FROM fact_economic_indicator f
JOIN dim_country c
ON f.country_id = c.country_id
WHERE f.indicator_id = 1
AND f.year = 2024
ORDER BY f.value DESC;

SELECT
    f.year,
    f.value
FROM fact_economic_indicator f
WHERE f.country_id = 4
AND f.indicator_id = 1
ORDER BY f.year;