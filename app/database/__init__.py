# app/__init__.py
# Inicializa o pacote principal da aplicação

from .connection import database_connection
from .querys import forma_map, categoria_map, inserir_mensagem_coletada, verifica_ultima_coleta