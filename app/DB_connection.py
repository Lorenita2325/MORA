import os
import mysql.connector
from dotenv import load_dotenv

load_dotenv()

def get_db_connection():
    return mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME")
    )

if __name__ == "__main__":
    try:
        connection = get_db_connection()
        print("Conexión exitosa a la base de datos")
        connection.close()
    except mysql.connector.Error as err:
        print(f"Error al conectar: {err}")
