import sqlite3
import pandas as pd

conn = sqlite3.connect("ecommerce.db")

# Example query: join customers, orders, and payments
query = """
SELECT 
    c.name AS customer_name,
    c.email,
    o.order_id,
    o.order_date,
    p.amount,
    p.payment_method
FROM customers c
JOIN orders o ON c.customer_id = o.customer_id
JOIN payments p ON o.order_id = p.order_id
WHERE o.status = 'Delivered'
ORDER BY o.order_date DESC;
"""

df = pd.read_sql_query(query, conn)
print(df.head())

df.to_csv("joined_output.csv", index=False)
print("✅ Joined data saved to joined_output.csv")

conn.close()
