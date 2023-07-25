import mysql.connector
def create_database():
    # Connect to the MySQL server
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="1234"
    )

    # Create a cursor to execute SQL queries
    cursor = connection.cursor()

    # Create the database if it does not exist
    cursor.execute("CREATE DATABASE IF NOT EXISTS cadastro")

    # Close the cursor and connection
    cursor.close()
    connection.close()