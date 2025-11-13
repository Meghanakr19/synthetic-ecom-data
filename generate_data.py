from faker import Faker
import pandas as pd
import random

fake = Faker()

# 1. Customers
customers = []
for i in range(1, 51):
    customers.append({
        "customer_id": i,
        "name": fake.name(),
        "email": fake.email(),
        "address": fake.address()
    })
pd.DataFrame(customers).to_csv("customers.csv", index=False)

# 2. Products
products = []
for i in range(1, 21):
    products.append({
        "product_id": i,
        "product_name": fake.word(),
        "category": random.choice(["Electronics", "Clothing", "Books", "Home", "Beauty"]),
        "price": round(random.uniform(5, 500), 2)
    })
pd.DataFrame(products).to_csv("products.csv", index=False)

# 3. Orders
orders = []
for i in range(1, 101):
    orders.append({
        "order_id": i,
        "customer_id": random.randint(1, 50),
        "order_date": fake.date_this_year(),
        "status": random.choice(["Pending", "Shipped", "Delivered", "Cancelled"])
    })
pd.DataFrame(orders).to_csv("orders.csv", index=False)

# 4. Order Items
order_items = []
for i in range(1, 201):
    order_items.append({
        "item_id": i,
        "order_id": random.randint(1, 100),
        "product_id": random.randint(1, 20),
        "quantity": random.randint(1, 5)
    })
pd.DataFrame(order_items).to_csv("order_items.csv", index=False)

# 5. Payments
payments = []
for i in range(1, 101):
    payments.append({
        "payment_id": i,
        "order_id": i,
        "payment_method": random.choice(["Credit Card", "PayPal", "Cash on Delivery"]),
        "amount": round(random.uniform(10, 1000), 2)
    })
pd.DataFrame(payments).to_csv("payments.csv", index=False)

print("✅ Synthetic e-commerce data generated successfully!")
