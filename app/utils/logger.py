import logging

def log_builder(logger_name):
        logger = logging.getLogger(logger_name)
        logger.setLevel(logging.DEBUG)
        file_handler = logging.FileHandler(
            r"C:\Users\Pedro Henrique\Desktop\RPA_FINANC\App\utils\log_aplicacao.txt"
        )
        file_handler.setLevel(logging.DEBUG) 
        formatter = logging.Formatter('%(asctime)s / %(levelname)s / %(name)s / %(funcName)s / %(message)s / line: %(lineno)d')
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
        return logger