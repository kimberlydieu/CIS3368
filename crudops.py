import mysql.connector
import creds
from mysql.connector import Error
from sql import create_connection
from sql import execute_query
from sql import execute_read_query

myCreds = creds.Creds()
conn = create_connection(myCreds.conString, myCreds.userName, myCreds.password, myCreds.dbName)

query = "INSERT INTO sales (seller, product, quantity, price) VALUES ('Jake', 'Hotdogs', 50, 1.50 )"
execute_query(conn, query)