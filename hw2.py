from flask import Flask
from flask import jsonify
from flask import request
import mysql.connector
from mysql.connector import Error

#database connection
import mysql.connector
from mysql.connector import Error

def create_con(hostname, username, pwd, dbname):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=hostname,
            user=username,
            password=pwd,
            database=dbname
        )
        print("Success: Connected to the database")
    except Error as e:
        print("Error: The error occurred at:", e)
    return connection

conn = create_con('cis3368fall.cplpsxg0kzbu.us-east-1.rds.amazonaws.com', 'admin', '12345678', 'cis3368')
cursor = conn.cursor(dictionary=True)
sql = 'SELECT * FROM zoo'
cursor.execute(sql)
rows = cursor.fetchall()

# test printing data from table
# for row in rows:
#     print(row)

cursor.close()
conn.close()


# GET REQUEST | return all animals from the zoo | running on http://127.0.0.1:5000/animals

app = Flask(__name__)
@app.route('/animals', methods=['GET'])
def get_animals():
    try:
        connection = mysql.connector.connect(
            host='cis3368fall.cplpsxg0kzbu.us-east-1.rds.amazonaws.com',
            user='admin',
            password='12345678',
            database='cis3368'
        )
        cursor = connection.cursor(dictionary=True)

        cursor.execute('SELECT * FROM zoo')
        animals = cursor.fetchall()

        return jsonify(animals)

    except Exception as e:
        return jsonify({'error': str(e)})

    finally:
        if 'connection' in locals() and connection.is_connected():
            cursor.close()
            connection.close()
            
if __name__ == '__main__':
    app.run(debug=True)


# POST


