# Data Sources

## 1. Primary Data Source — World Bank

The World Bank will be the primary data source for Version 1 of the project.

### Indicators

| Indicator                 | Code         | Source     |
| ------------------------- | ------------ | ---------- |
| GDP Growth                | GDP_GROWTH   | World Bank |
| GDP per Capita            | GDP_PC       | World Bank |
| Inflation                 | INFLATION    | World Bank |
| Unemployment              | UNEMPLOYMENT | World Bank |
| Foreign Direct Investment | FDI          | World Bank |
| Exports                   | EXPORTS      | World Bank |
| Imports                   | IMPORTS      | World Bank |
| Population                | POPULATION   | World Bank |

The World Bank Indicators API will be used for programmatic
country, indicator, and year queries.

## 2. Secondary Data Source — IMF

The IMF will be used as a secondary source for validation
and comparison where applicable.

## 3. Countries

The project will initially cover the following nine countries:

- Benin
- Burkina Faso
- Côte d'Ivoire
- Ghana
- Guinea
- Liberia
- Mali
- Senegal
- Sierra Leone

## 4. Data Collection Approach

The pipeline will:

1. Request data from the World Bank API.
2. Store the original responses as raw data.
3. Validate the returned data.
4. Transform the data into the project's standardized structure.
5. Store processed data for analysis.
6. Use IMF data for secondary validation where applicable.

## 5. Data Principles

- Raw data will not be modified.
- Source information will be preserved.
- Data transformations will be reproducible.
- Missing values will be handled explicitly.
- Indicator definitions and units will be documented.
- Country identifiers will use ISO3 codes.
