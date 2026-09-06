CREATE VIEW regional_gdp_growth AS
SELECT
    f.year,
    AVG(f.value) AS regional_gdp_growth
FROM fact_economic_indicator f
WHERE f.indicator_id = 1
GROUP BY f.year
ORDER BY f.year;

CREATE VIEW regional_inflation AS
SELECT
    f.year,
    AVG(f.value) AS regional_inflation
FROM fact_economic_indicator f
WHERE f.indicator_id = 3
GROUP BY f.year
ORDER BY f.year;

CREATE VIEW average_gdp_per_capita AS
SELECT
    f.year,
    AVG(f.value) AS average_gdp_per_capita
FROM fact_economic_indicator f
WHERE f.indicator_id = 2
GROUP BY f.year
ORDER BY f.year;

CREATE VIEW debt_trend AS
SELECT
    f.year,
    AVG(f.value) AS average_government_debt
FROM fact_economic_indicator f
WHERE f.indicator_id = 5
GROUP BY f.year
ORDER BY f.year;

CREATE VIEW fdi_trend AS
SELECT
    f.year,
    AVG(f.value) AS average_fdi
FROM fact_economic_indicator f
WHERE f.indicator_id = 6
GROUP BY f.year
ORDER BY f.year;

CREATE VIEW trade_balance AS
SELECT
    e.year,
    e.value - i.value AS trade_balance
FROM fact_economic_indicator e
JOIN fact_economic_indicator i
    ON e.country_id = i.country_id
    AND e.year = i.year
WHERE e.indicator_id = 7
AND i.indicator_id = 8
ORDER BY e.year;