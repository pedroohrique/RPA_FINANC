from app.utils.logger import log_builder
from app.database.connection import database_connection

log = log_builder("querys.py") 



def forma_map() -> dict:
    connection, cursor = database_connection()
    try:        
        with connection:
            query = "SELECT DESCRICAO, ID_FORMA FROM TB_FORMA_PAGAMENTO"
            cursor.execute(query)
            retorno_query = cursor.fetchall()
            formas = {linha[0]:linha[1] for linha in retorno_query}    
        return formas
    except Exception as e:
        log.error(f"Falha ao executar a query: {e}")
    finally:
        cursor.close()
        
def categoria_map() -> dict:
    connection, cursor = database_connection()
    try:        
        with connection:
            query = "SELECT DESCRICAO, ID_CATEGORIA FROM TB_CATEGORIA"
            cursor.execute(query)
            retorno_query = cursor.fetchall()
            categorias = {linha[0].upper():linha[1] for linha in retorno_query}
        return categorias
    except Exception as e:
        log.error(f"Erro ao executar a query: {e}")
    finally:
        cursor.close()
        

def verifica_ultima_coleta():     
    connection, cursor = database_connection()    
    try:
        with connection:             
            query = "SELECT TOP 1 ID_COLETA FROM TB_MENSAGENS_COLETADAS ORDER BY ID_COLETA DESC"
            cursor.execute(query)
            retorno_query = cursor.fetchone()            
        return retorno_query[0] if retorno_query else 0
    except (ValueError, TypeError) as e:                        
        log.error(f"Erro ao verificar a última mensagem: {e}")
    finally:
        cursor.close()
        
        
        

def inserir_mensagem_coletada(dicionario):  
    connection, cursor = database_connection()   
    query_TMC = "INSERT INTO TB_MENSAGENS_COLETADAS (ID_COLETA, DATA_COLETA, DATA_GASTO, DESCRICAO) VALUES (?, GETDATE(), ?, ?)"
    query_TRF = "INSERT INTO TB_REG_FINANC (DATA_REGISTRO, DATA_GASTO, VALOR, DESCRICAO, LOCAL_GASTO, PARCELAMENTO, N_PARCELAS, IDCATEGORIA, IDFORMA_PAGAMENTO) VALUES (GETDATE(), ?, ?, ?, ?, ?, ?, ?, ?)"
    required_keys = ['ID', 'Data Compra', 'Valor', 'Desc', 'Local', 'Forma', 'Parcelamento', 'QTD Parcelas', 'Categoria']
    
    if not all(key in dicionario for key in required_keys):
        log.error(f"Chaves faltando: {required_keys}")
        return False

    try:        
        with connection:            
            cursor.execute(
                query_TMC,(dicionario['ID'], dicionario['Data Compra'], dicionario['Desc'])
            )
            cursor.execute(
                query_TRF,
                (
                 dicionario['Data Compra'], 
                 dicionario['Valor'], 
                 dicionario['Desc'], 
                 dicionario['Local'], 
                 dicionario['Parcelamento'], 
                 dicionario['QTD Parcelas'], 
                 dicionario['Categoria'],
                 dicionario['Forma'],)
            )
            log.info(f"Mensagem coletada com sucesso! ID: {dicionario['ID']}")
            dicionario.clear()
            return True

    except Exception as e:
        log.error(f"Falha ao inserir no banco: {e}")
        return False
    finally:
        cursor.close()



