from app.utils.logger import log_builder
from app.database.querys import verifica_ultima_coleta, forma_map, categoria_map, inserir_mensagem_coletada

log = log_builder("data_handler")



def handler(mensagens):    
    mensagens_processadas = []
    id_ultima_coleta = verifica_ultima_coleta()
    formas = forma_map()
    categorias = categoria_map()

    for array in mensagens:
        try:            
            if len(array) != 9:
                raise ValueError(f"Mensagem fora do padrão esperado! {array}")            
            if int(array[0]) > id_ultima_coleta:
                dados = {
                'ID': int(array[0].strip()),
                'Data Compra': str(array[1].strip()),
                'Valor': float(array[2].strip()),
                'Desc': str(array[3].strip()),
                'Local': str(array[4].strip()),
                'Forma': formas.get(array[5].strip().upper()),
                'Parcelamento': str(array[6].strip().upper()),
                'QTD Parcelas': int(array[7].strip()),
                'Categoria': categorias.get(array[8].strip().upper())
            }
                mensagens_processadas.append(dados)          

        except Exception as e:
            log.error(f"Erro ao processar a mensagem: {e}")
                
    if len(mensagens_processadas) == 0:
        log.info(f"Não há mensagens para processar, último ID coletado {id_ultima_coleta}")
    else:        
        for mensagem in mensagens_processadas:
            inserir_mensagem_coletada(mensagem)



