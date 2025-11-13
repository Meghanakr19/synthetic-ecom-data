import pandas as pd
import sqlite3

# Connect to SQLite database (creates file if not exists)
conn = sqlite3.connect("ecommerce.db")

# Load CSVs
files = {
    "customers": "customers.csv",
    "products": "products.csv",
    "orders": "orders.csv",
    "order_items": "order_items.csv",
    "payments": "payments.csv"
}

for table_name, file_name in files.items():
    df = pd.read_csv(file_name)
    df.to_sql(table_name, conn, if_exists="replace", index=False)
    print(f"✅ Loaded {table_name} into SQLite database")

conn.close()
print("✅ All tables loaded successfully into ecommerce.db")
