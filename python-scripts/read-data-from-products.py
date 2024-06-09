import psycopg2

# Connect to the database
conn = psycopg2.connect(
    dbname='productdb',
    user='postgres',
    password='p0stgres',
    host='localhost',
    port='5432'
)

# create a cursor
cur = conn.cursor()

# select all data from the products table
select_query = '''
SELECT * FROM products;
'''

cur.execute(select_query)
rows = cur.fetchall()

# processing data
for row in rows:
    print(f"ProductID: {row[0]}, ProductName: {row[1]}, Price: {row[2]}, Category: {row[3]}")

# close communication with the database
cur.close()
conn.close()
