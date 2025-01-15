from flask import Flask, request, jsonify
import mysql.connector
from mysql.connector import Error
import os

app = Flask(__name__)

# Conexión a la base de datos MySQL usando variables de entorno
def connect_to_db():
    try:
        conn = mysql.connector.connect(
            host=os.getenv("DB_HOST"),
            database=os.getenv("DB_CREATE_DATABASE"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD")
        )
        if conn.is_connected():
            return conn
    except Error as e:
        print(f"Error al conectar a MySQL: {e}")
        return None

# Endpoint para registrar un cliente
@app.route('/customer', methods=['POST'])
def create_customer():
    data = request.json

    # Validación de los datos recibidos
    if not all(key in data for key in ('FirstName', 'LastName', 'Email', 'PhoneNumber')):
        return jsonify({"message": "Missing required fields"}), 400

    conn = connect_to_db()
    if conn:
        cursor = conn.cursor()
        try:
            cursor.execute(
                "INSERT INTO Customers (FirstName, LastName, Email, PhoneNumber) VALUES (%s, %s, %s, %s)",
                (data['FirstName'], data['LastName'], data['Email'], data['PhoneNumber'])
            )
            conn.commit()
            return jsonify({"message": "Customer created successfully!"}), 201
        except Error as e:
            return jsonify({"message": f"Failed to insert customer: {e}"}), 500
        finally:
            cursor.close()
            conn.close()

    return jsonify({"message": "Failed to connect to database"}), 500

# Iniciar la aplicación
if __name__ == "__main__":
    app.run(debug=True)
