import os
import pyodbc
from dotenv import load_dotenv
from app.utils.logger import log_builder

log = log_builder("database.py")
load_dotenv()

def database_connection():
    server = os.getenv("DB_SERVER")
    database = os.getenv("DB_DATABASE")
    username = os.getenv("DB_USER")
    password = os.getenv("DB_PASSWORD")

    try:
        connection = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + server + ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password)
        cursor = connection.cursor()
        return connection, cursor

    except pyodbc.Error as e:        
        log.error(f"Falha ao conectar ao banco de dados local: {e}")
        return None