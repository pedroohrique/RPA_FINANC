import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from app.utils.logger import configura_log

log = configura_log("browser.py")


def configura_driver():    
    try:
        chromedriver_path = os.getenv("CHROMEDRIVER_PATH", r"C:\\Windows\\System32\\chromedriver-win64\\chromedriver.exe")
        chrome_binary = os.getenv("CHROME_PATH", r"C:\\Program Files\\chrome-win64\\chrome.exe")
        service = Service(chromedriver_path)
        options = webdriver.ChromeOptions()
        options.binary_location = chrome_binary
        options.add_argument(r"user-data-dir=C:\\whatappcache")
        options.add_argument("--profile-directory=Default")
        driver = webdriver.Chrome(service=service, options=options)
        return driver
    
    except Exception as e:
        log.error(f"Falha ao configurar o browser {e}")