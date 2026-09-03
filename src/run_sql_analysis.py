import sqlite3

# Database
database_file = "database/economic_analysis.db"

# Connect to database
connection = sqlite3.connect(database_file)

cursor = connection.cursor()

print("SQL Economic Analysis")
print("=====================")

# 1. GDP Growth
print("\n1. GDP Growth by Country")
print("------------------------")

cursor.execute("""
SELECT
    country,
    value AS gdp_growth
FROM economic_analysis_2024
WHERE indicator = 'GDP_GROWTH'
ORDER BY gdp_growth DESC;
""")

for row in cursor.fetchall():
    print(row)


# 2. GDP per Capita
print("\n2. GDP Per Capita by Country")
print("----------------------------")

cursor.execute("""
SELECT
    country,
    value AS gdp_per_capita
FROM economic_analysis_2024
WHERE indicator = 'GDP_PC'
ORDER BY gdp_per_capita DESC;
""")

for row in cursor.fetchall():
    print(row)


# 3. Inflation
print("\n3. Inflation by Country")
print("----------------------")

cursor.execute("""
SELECT
    country,
    value AS inflation
FROM economic_analysis_2024
WHERE indicator = 'INFLATION'
ORDER BY inflation DESC;
""")

for row in cursor.fetchall():
    print(row)


# 4. Unemployment
print("\n4. Unemployment by Country")
print("-------------------------")

cursor.execute("""
SELECT
    country,
    value AS unemployment
FROM economic_analysis_2024
WHERE indicator = 'UNEMPLOYMENT'
ORDER BY unemployment DESC;
""")

for row in cursor.fetchall():
    print(row)


connection.close()

print("\nSQL analysis completed successfully.")