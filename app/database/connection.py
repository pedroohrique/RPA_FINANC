import json
import pyodbc
from app.utils.logger import log_builder

log = log_builder("database.py")

def load_config():
    config_path = r"app\database\config.json"
    try:
        with open(config_path, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        raise Exception(log.error(f"Arquivo de configuração não encontrado em: {config_path}"))

def database_connection():
    database_config = load_config()
    server = database_config["database"]["server"]
    database = database_config["database"]["name"]
    username = database_config["database"]["user"]
    password = database_config["database"]["password"]

    # Verificação rápida
    if not all([server, database, username, password]):
        log.error("Uma ou mais variáveis de ambiente do banco não foram carregadas.")
        log.debug(f"SERVER: {server}, DATABASE: {database}, USER: {username}, PASSWORD: {password}")
        return None

    try:
        connection = pyodbc.connect(
            'DRIVER={ODBC Driver 17 for SQL Server};'
            f'SERVER={server};DATABASE={database};UID={username};PWD={password}'
        )
        cursor = connection.cursor()
        return connection, cursor

    except pyodbc.Error as e:        
        log.error(f"Falha ao conectar ao banco de dados local: {e}")
        return None

