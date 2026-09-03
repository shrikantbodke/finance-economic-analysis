import sqlite3
import pandas as pd

# Input CSV
input_file = "data/final/economic_analysis_2024.csv"

# SQLite database
database_file = "database/economic_analysis.db"

# Load CSV
df = pd.read_csv(input_file)

# Connect to SQLite database
connection = sqlite3.connect(database_file)

# Load data into database table
df.to_sql(
    "economic_analysis_2024",
    connection,
    if_exists="replace",
    index=False
)

print("Database created successfully.")
print("Table: economic_analysis_2024")
print("Rows loaded:", len(df))

# Close connection
connection.close()