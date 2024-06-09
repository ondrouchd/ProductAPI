import psycopg2

conn = psycopg2.connect(
    dbname='productdb',
    user='postgres',
    password='p0stgres',
    host='localhost',
    port='5432'
)

# create a cursor
cur = conn.cursor()

# create a table named products
create_table_query = '''
CREATE TABLE products (
    ProductID SERIAL PRIMARY KEY,
    ProductName VARCHAR(255) NOT NULL,
    Price DECIMAL(10, 2) NOT NULL,
    Category VARCHAR(255) NOT NULL
);
'''

cur.execute(create_table_query)

# close communication with the database
cur.close()
conn.commit()
conn.close()