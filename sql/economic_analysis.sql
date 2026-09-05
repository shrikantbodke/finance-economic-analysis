-- Finance & Economic Intelligence Platform
-- 2024 Economic Analysis

-- 1. View the complete 2024 dataset
SELECT *
FROM economic_analysis_2024;


-- 2. GDP growth by country
SELECT
    country,
    value AS gdp_growth
FROM economic_analysis_2024
WHERE indicator = 'GDP_GROWTH'
ORDER BY gdp_growth DESC;


-- 3. GDP per capita by country
SELECT
    country,
    value AS gdp_per_capita
FROM economic_analysis_2024
WHERE indicator = 'GDP_PC'
ORDER BY gdp_per_capita DESC;


-- 4. Inflation by country
SELECT
    country,
    value AS inflation
FROM economic_analysis_2024
WHERE indicator = 'INFLATION'
ORDER BY inflation DESC;


-- 5. Unemployment by country
SELECT
    country,
    value AS unemployment
FROM economic_analysis_2024
WHERE indicator = 'UNEMPLOYMENT'
ORDER BY unemployment DESC;

-- 6. Government Debt by country
SELECT
    c.country_name,
    f.year,
    f.value AS government_debt
FROM public.fact_economic_indicator f
JOIN public.dim_country c
    ON f.country_id = c.country_id
JOIN public.dim_indicator i
    ON f.indicator_id = i.indicator_id
WHERE i.indicator_code = 'GOV_DEBT'
ORDER BY f.year, government_debt DESC;


-- 7. FDI by country
SELECT
    c.country_name,
    f.year,
    f.value AS fdi
FROM public.fact_economic_indicator f
JOIN public.dim_country c
    ON f.country_id = c.country_id
JOIN public.dim_indicator i
    ON f.indicator_id = i.indicator_id
WHERE i.indicator_code = 'FDI'
ORDER BY f.year, fdi DESC;


-- 8. Exports by country
SELECT
    c.country_name,
    f.year,
    f.value AS exports
FROM public.fact_economic_indicator f
JOIN public.dim_country c
    ON f.country_id = c.country_id
JOIN public.dim_indicator i
    ON f.indicator_id = i.indicator_id
WHERE i.indicator_code = 'EXPORTS'
ORDER BY f.year, exports DESC;


-- 9. Imports by country
SELECT
    c.country_name,
    f.year,
    f.value AS imports
FROM public.fact_economic_indicator f
JOIN public.dim_country c
    ON f.country_id = c.country_id
JOIN public.dim_indicator i
    ON f.indicator_id = i.indicator_id
WHERE i.indicator_code = 'IMPORTS'
ORDER BY f.year, imports DESC;


-- 10. Current Account Balance by country
SELECT
    c.country_name,
    f.year,
    f.value AS current_account_balance
FROM public.fact_economic_indicator f
JOIN public.dim_country c
    ON f.country_id = c.country_id
JOIN public.dim_indicator i
    ON f.indicator_id = i.indicator_id
WHERE i.indicator_code = 'CURRENT_ACCOUNT'
ORDER BY f.year, current_account_balance DESC;


-- 11. Population by country
SELECT
    c.country_name,
    f.year,
    f.value AS population
FROM public.fact_economic_indicator f
JOIN public.dim_country c
    ON f.country_id = c.country_id
JOIN public.dim_indicator i
    ON f.indicator_id = i.indicator_id
WHERE i.indicator_code = 'POPULATION'
ORDER BY f.year, population DESC;