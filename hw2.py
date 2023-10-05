from flask import Flask
from flask import jsonify
from flask import request
import mysql.connector



#database connection
config = {
    'user': 'admin',
    'password': '12345678',
    'host': 'cis3368fall.cplpsxg0kzbu.us-east-1.rds.amazonaws.com',  
    'database': 'cis3368',
    'raise_on_warnings': True
}

try:
    connection = mysql.connector.connect(**config)

    if connection.is_connected():
        print("Connected to MySQL database")
        
        
except mysql.connector.Error as err:
    print(f"Error: {err}")
finally:

    if 'connection' in locals() and connection.is_connected():
        connection.close()
        print("Connection closed")




# app= Flask(__name__)
# @app.route('/')
# def home():
#     return "hey"



# app.run(port=7780)