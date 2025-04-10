from app.services.scrap import parser
from app.services.data_handler import handler
from app.utils.logger import configura_log

log = configura_log("coleta.py")

class AutomacaoColeta:
    def __init__(self):
        self.coletar()

    def coletar(self):
        try:
            dados = parser()
        except Exception as e:
            log.error(f"Erro ao coletar os dados: {e}")
            return

        try:
            handler(dados)
        except Exception as e:
            log.error(f"Erro ao processar os dados coletados: {e}")
        