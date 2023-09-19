#importing sql
import mysql.connector
from mysql.connector import Error

def create_con(hostname, username, pwd,dbname):
    connection = None
    try:
        connection = mysql.connector.connect(
            host = hostname,
            user = username,
            password = pwd,
            database = dbname
        )
        print("success")
    except Error as e:
        print("the error occured at : ", e)
    return connection

conn = create_con('cis3368fall.cplpsxg0kzbu.us-east-1.rds.amazonaws.com','admin','12345678','cis3368')
cursor = conn.cursor(dictionary = True)
sql = 'select * from sales'
cursor.execute(sql)
rows = cursor.fetchall()

# User Interface
print("Which seller would you like to access?")
for sales_dict in rows:
    print(sales_dict['seller'])

# Asking which seller user wants
pick_seller = input("Enter your seller name here.")

# Returning sales information based on what user inputted
if pick_seller == rows[0]['seller']:
    print("Sales Report for", rows[0]['seller'])
    print("Product:", rows[0]['product'])
    print("Quantity:", rows[0]['quantity'])
    print("Price:", rows[0]['price'])
    print("Total sales for", rows[0]['seller'],"are $", rows[0]['quantity'] * rows[0]['price'])

if pick_seller == rows[1]['seller']:
    print("Sales Report for", rows[1]['seller'])
    print("Product:", rows[1]['product'])
    print("Quantity:", rows[1]['quantity'])
    print("Price:", rows[1]['price'])
    print("Total sales for", rows[1]['seller'],"are $", rows[1]['quantity'] * rows[1]['price'])

if pick_seller == rows[2]['seller']:
    print("Sales Report for", rows[2]['seller'])
    print("Product:", rows[2]['product'])
    print("Quantity:", rows[2]['quantity'])
    print("Price:", rows[2]['price'])
    print("Total sales for", rows[2]['seller'],"are $", rows[2]['quantity'] * rows[2]['price'])

if pick_seller == rows[3]['seller']:
    print("Sales Report for", rows[3]['seller'])
    print("Product:", rows[3]['product'])
    print("Quantity:", rows[3]['quantity'])
    print("Price:", rows[3]['price'])
    print("Total sales for", rows[3]['seller'],"are $", rows[3]['quantity'] * rows[3]['price'])

if pick_seller == rows[4]['seller']:
    print("Sales Report for", rows[4]['seller'])
    print("Product:", rows[4]['product'])
    print("Quantity:", rows[4]['quantity'])
    print("Price:", rows[4]['price'])
    print("Total sales for", rows[4]['seller'],"are $", rows[4]['quantity'] * rows[4]['price'])

if pick_seller == rows[5]['seller']:
    print("Sales Report for", rows[5]['seller'])
    print("Product:", rows[5]['product'])
    print("Quantity:", rows[5]['quantity'])
    print("Price:", rows[5]['price'])
    print("Total sales for", rows[5]['seller'],"are $", rows[5]['quantity'] * rows[5]['price'])

if pick_seller == rows[6]['seller']:
    print("Sales Report for", rows[6]['seller'])
    print("Product:", rows[6]['product'])
    print("Quantity:", rows[6]['quantity'])
    print("Price:", rows[6]['price'])
    print("Total sales for", rows[6]['seller'],"are $", rows[6]['quantity'] * rows[6]['price'])

if pick_seller == rows[7]['seller']:
    print("Sales Report for", rows[7]['seller'])
    print("Product:", rows[7]['product'])
    print("Quantity:", rows[7]['quantity'])
    print("Price:", rows[7]['price'])
    print("Total sales for", rows[7]['seller'],"are $", rows[7]['quantity'] * rows[7]['price'])

if pick_seller == rows[8]['seller']:
    print("Sales Report for", rows[8]['seller'])
    print("Product:", rows[8]['product'])
    print("Quantity:", rows[8]['quantity'])
    print("Price:", rows[8]['price'])
    print("Total sales for", rows[8]['seller'],"are $", rows[8]['quantity'] * rows[8]['price'])

if pick_seller == rows[9]['seller']:
    print("Sales Report for", rows[9]['seller'])
    print("Product:", rows[9]['product'])
    print("Quantity:", rows[9]['quantity'])
    print("Price:", rows[9]['price'])
    print("Total sales for", rows[9]['seller'],"are $", rows[9]['quantity'] * rows[9]['price'])