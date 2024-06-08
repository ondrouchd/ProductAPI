import psycopg2
import random

conn = psycopg2.connect(
    dbname='productdb',
    user='postgres',	
    password='p0stgres',
    host='localhost',
    port='5432'
)

# create a cursor
cur = conn.cursor()

# insert data into the products table
insert_data_query = '''
INSERT INTO products (ProductName, Price, Category)
VALUES (%s, %s, %s);
'''

# thousands of records to insert

# the list of potrential products, prices, and categories
product_names = ['Laptop', 'Hammer', 'Basketball', 'Shirt', 'Pants', 'Hat', 'Shoes', 'Socks', 'Gloves', 'Jacket']
prices = [1000.00, 10.00, 20.00, 30.00, 40.00, 50.00, 60.00, 70.00, 80.00, 90.00, 100.00, 110.00, 120.00, 130.00, 140.00, 150.00, 160.00, 170.00, 180.00, 190.00, 200.00]   
categories = ['Electronics', 'Tools', 'Sports', 'Clothing', 'Kitchen', 'Outdoors', 'Automotive', 'Toys', 'Books', 'Music', 'Movies', 'Health', 'Beauty', 'Food', 'Drinks', 'Furniture', 'Jewelry', 'Pets', 'Garden', 'Office']

# generate random data
data_to_insert = []
for i in range(5000):
    product_name = random.choice(product_names)
    price = random.choice(prices)
    category = random.choice(categories)
    record = (product_name, price, category)
    data_to_insert.append((product_name, price, category))


# insert each record of data
for record in data_to_insert:
    cur.execute(insert_data_query, record)

# close communication with the database
cur.close()
conn.commit()
conn.close()