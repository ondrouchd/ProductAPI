import psycopg2
from psycopg2 import sql

# Connect to the postgresql database
conn = psycopg2.connect(
    dbname='postgres',
    user='postgres',	
    password='p0stgres',
    host='localhost',
    port='5432'
)

conn.autocommit = True

# create cursor 
cur = conn.cursor()

# create a new database	
cur.execute('CREATE DATABASE productdb')	

# close communication with the database
cur.close()
conn.close()

