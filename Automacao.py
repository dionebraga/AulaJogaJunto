from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from webdriver_manager.firefox import GeckoDriverManager
import time

# Configuração do Firefox
options = FirefoxOptions()
options.add_argument("--headless")  # Executa o navegador em modo headless (sem interface gráfica)
service = FirefoxService(GeckoDriverManager().install())  # Gerencia a instalação do geckodriver

# Inicializa o navegador
browser = webdriver.Firefox(service=service, options=options)

try:
    # Realizar uma pesquisa no Google
    query = "site:jogajuntoinstituto.org"
    browser.get(f"https://www.google.com/search?q={query}")

    # Esperar para resultados carregarem
    time.sleep(3)

    # Clicar no primeiro resultado do Google
    first_result = browser.find_element(By.CSS_SELECTOR, "h3")
    first_result.click()

    # Esperar a página carregar
    time.sleep(3)

    # Navegar para a página de contato
    contact_link = browser.find_element(By.LINK_TEXT, "Contato")
    contact_link.click()

    # Esperar a página de contato carregar
    time.sleep(3)

    # Preencher o formulário de contato
    name_field = browser.find_element(By.NAME, "your-name")
    email_field = browser.find_element(By.NAME, "your-email")
    subject_field = browser.find_element(By.NAME, "your-subject")
    message_field = browser.find_element(By.NAME, "your-message")

    name_field.send_keys("Dione Braga")
    email_field.send_keys("dionebraga.work@gmail.com")
    subject_field.send_keys("Eu quero ser Facilitador")
    message_field.send_keys("Eu quero ser Facilitador")

    # Enviar o formulário
    send_button = browser.find_element(By.XPATH, "//input[@type='Enviar']")
    send_button.click()

    # Esperar a página processar o envio
    time.sleep(5)

finally:
    # Fechar o navegador ao finalizar
    browser.quit()
