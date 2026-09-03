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