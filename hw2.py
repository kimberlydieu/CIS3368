from flask import Flask
from flask import jsonify
from flask import request
import mysql.connector
from mysql.connector import Error

# testing database connection

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
        print("Could not connect to database")
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

app = Flask(__name__)

# connecting to db
db_config = {
    'host': 'cis3368fall.cplpsxg0kzbu.us-east-1.rds.amazonaws.com',
    'user': 'admin',
    'password': '12345678',
    'database': 'cis3368',
}

def get_db_connection():
    try:
        connection = mysql.connector.connect(**db_config)
        return connection
    except Error as e:
        print(f"Error: {e}")
        return None

# GET animals in zoo
@app.route('/animals', methods=['GET'])
def get_animals():
    try:
        connection = get_db_connection()
        cursor = connection.cursor(dictionary=True)
        cursor.execute('SELECT * FROM zoo')
        animals = cursor.fetchall()
        return jsonify(animals)
    except Exception as e:
        return jsonify({'error': str(e)})
    finally:
            cursor.close()
            connection.close()

# POST/Add animals in zoo
# post body template example
# {
#     "age": "36",
#     "alive": "0",
#     "animalname": "elle",
#     "class": "Mammalia",
#     "domain": "Eukarya",
#     "kingdom": "Animalia",
#     "species": "Elephant"
# }
@app.route('/animals', methods=['POST'])
def add_animal():
    try:
        connection = get_db_connection()
        cursor = connection.cursor()
        data = request.get_json()

        if 'animalname' in data and 'species' in data:
            cursor.execute("INSERT INTO zoo (age, alive, animalname, class, domain, kingdom, species) VALUES (%s,%s,%s,%s,%s,%s,%s)",
                           (data['age'], data['alive'],data['animalname'],data['class'],data['domain'],data['kingdom'],data['species']))
            connection.commit()
            return jsonify({'message': 'Animal added successfully'})
        else:
            return jsonify({'error': 'Could not add animal'})

    except Exception as e:
        return jsonify({'error': str(e)})
    finally:
            cursor.close()
            connection.close()

# DELETE Animals in Zoo by ID 
# http://127.0.0.1:5000/animals/(put animal id number here)
@app.route('/animals/<int:id>', methods=['DELETE'])
def delete_animal(id):
    try:
        connection = get_db_connection()
        cursor = connection.cursor()
        cursor.execute("DELETE FROM zoo WHERE id = %s", (id,))
        connection.commit()
        return jsonify({'message': 'Animal deleted'})

    except Exception as e:
        return jsonify({'error': str(e)})
    finally:
            cursor.close()
            connection.close()

# PUT/Update Animals in Zoo
@app.route('/animals/<int:id>', methods=['PUT'])
def update_animal(id):
    try:
        connection = get_db_connection()
        cursor = connection.cursor()
        data = request.get_json()

        if 'animalname' in data and 'species' in data:
            cursor.execute("UPDATE zoo SET age = %s, alive = %s, animalname= = %s, class = %s, domain = %s, kingdom = %s, species = %s WHERE id = %s",
                           (data['age'], data['alive'],data['animalname'],data['class'],data['domain'],data['kingdom'],data['species'], id,))
            connection.commit()
            return jsonify({'message': 'Animal updated'})
        else:
            return jsonify({'error': 'Animal could not be updated'})

    except Exception as e:
        return jsonify({'error': str(e)})
    finally:
        if 'connection' in locals() and connection.is_connected():
            cursor.close()
            connection.close()
            

if __name__ == '__main__':
    app.run(debug=True)



