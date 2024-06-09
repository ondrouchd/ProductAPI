import psycopg2
import pandas as pd
from faker import Faker
import random
from datetime import datetime, timedelta

# Connect to the database
conn = psycopg2.connect(
    host="localhost",
    database="productdb",
    user="postgres",
    password="p0stgres",
    port="5432",
)

# read the product table
query = "SELECT productid, productname, price, category FROM products"
products_df = pd.read_sql(query, conn)

# initialize the Faker object
fake = Faker()

# generate sales data
def generate_sales_data(products_df, num_orders=1000):
    sales_data = []
    for order_id in range(num_orders):
        product = products_df.sample().iloc[0]
        quantity = random.randint(1, 10)
        order_date = fake.date_between(start_date='-1y', end_date='today').strftime('%Y-%m-%d')
        total_price = product['price'] * quantity
        sales_data.append({
            'order_id': order_id,
            'product': product['productname'],
            'category': product['category'],
            'quantity': quantity,
            'price_per_unit': product['price'],
            'total_price': total_price,
            'order_date': order_date
        })
        
    return pd.DataFrame(sales_data)

# generate random sales data
sales_data_df = generate_sales_data(products_df)

# store the sales data into CSV file
sales_data_df.to_csv('assets/sales_data.csv', index=False)

# close connection to the database
conn.close()
    
