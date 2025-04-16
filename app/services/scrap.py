from app.utils.browser import configura_driver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from app.utils.logger import log_builder
import time as tempo_carregamento

log = log_builder("scrap.py")

def parser():
    try:        
        driver = configura_driver()
        driver.get("https://web.whatsapp.com")
        tempo_carregamento.sleep(3)
        
        elemento_caixa_pesquisa = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.CSS_SELECTOR, "p.selectable-text.copyable-text")))        
        elemento_caixa_pesquisa.send_keys("Financeiro")
        
        tempo_carregamento.sleep(3)
        
        elemeno_icone_grupo = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.CSS_SELECTOR, "span.matched-text")))
        elemeno_icone_grupo.click()
        
        elemento_chat = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.CSS_SELECTOR, "div[class*='x1vjfegm x1cqoux5 x14yy4lh']"))        )
        
        tempo_carregamento.sleep(3)
        
        mensagens = elemento_chat.find_elements(By.CSS_SELECTOR, "div[class*='_akbu']")
        array_mgs = [row.text.split('\n') for row in mensagens]
        
        log.info("Scrapy realizado com sucesso!")
        return array_mgs
        
    except (TimeoutException, NoSuchElementException, Exception) as e:
        log.error(f"Erro ao carregar ou encontrar os elementos: {e}")
