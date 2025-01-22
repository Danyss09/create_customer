from services.db_config import get_connection

def create_customer(first_name, last_name, email, phone_number, address):
    connection = get_connection()
    try:
        with connection.cursor() as cursor:
            query = """
            INSERT INTO Customers (FirstName, LastName, Email, PhoneNumber, Address)
            VALUES (%s, %s, %s, %s, %s)
            """
            cursor.execute(query, (first_name, last_name, email, phone_number, address))
            connection.commit()
            return {"message": "Customer created successfully!"}
    except Exception as e:
        return {"error": str(e)}
    finally:
        connection.close()

def get_all_customers():
    connection = get_connection()
    try:
        with connection.cursor() as cursor:
            query = "SELECT * FROM Customers"
            cursor.execute(query)
            customers = cursor.fetchall()
            return customers
    except Exception as e:
        return {"error": str(e)}
    finally:
        connection.close()
