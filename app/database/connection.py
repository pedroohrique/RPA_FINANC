import pyodbc
from app.utils.logger import configura_log

log = configura_log("database.py")

def database_connection():
    server = 'DESKTOP-98I4FGO'
    database = 'FINANCEIRO'
    user = 'Admin'
    password = '66tUa3ue'

    try:
        connection = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + server + ';DATABASE=' + database + ';UID=' + user + ';PWD=' + password)
        cursor = connection.cursor()
        return connection, cursor

    except pyodbc.Error as e:        
        log.error(f"Falha ao conectar ao banco de dados local: {e}")
        return None

