from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import time

# Configuração do Chrome para janela anônima
options = webdriver.ChromeOptions()
options.add_argument("--incognito")  # Abre o navegador em modo incógnito
# options.add_argument("--headless")   # Removido para interação visual durante o teste

# Inicializa o serviço do Chrome
service = ChromeService(ChromeDriverManager().install())

# Inicializa o navegador Chrome com as opções configuradas
browser = webdriver.Chrome(service=service, options=options)

try:
    # Termo de pesquisa no Google
    termo_pesquisa = "jogajuntoinstituto.org"

    # Abre o Google e faz a pesquisa
    browser.get("https://www.google.com/")
    campo_pesquisa = browser.find_element(By.NAME, "q")
    campo_pesquisa.send_keys(termo_pesquisa)
    campo_pesquisa.send_keys(Keys.RETURN)

    # Aguarda um momento para os resultados carregarem
    time.sleep(5)

    # Encontra e clica no primeiro link disponível
    resultados = browser.find_elements(By.XPATH, "//h3//parent::a")
    for resultado in resultados:
        if "jogajuntoinstituto.org" in resultado.get_attribute("href"):
            resultado.click()
            break

    # Espera a página carregar completamente
    time.sleep(10)

    # Navega até a página de contatos
    contato_link = browser.find_element(By.LINK_TEXT, "Contato")
    browser.execute_script("arguments[0].scrollIntoView(true);", contato_link)
    time.sleep(2)
    contato_link.click()

    # Espera a página de contatos carregar completamente
    time.sleep(10)

    # Scroll até o formulário de contato
    formulario_contato = browser.find_element(By.ID, "Contato")
    browser.execute_script("arguments[0].scrollIntoView();", formulario_contato)

    # Preenche os campos do formulário
    nome_input = browser.find_element(By.ID, "nome")
    nome_input.send_keys("Dione Braga")

    email_input = browser.find_element(By.ID, "email")
    email_input.send_keys("dionebraga.work@gmail.com")

    assunto_select = browser.find_element(By.ID, "assunto")
    assunto_select.send_keys("Ser facilitador")

    mensagem_textarea = browser.find_element(By.ID, "mensagem")
    mensagem_textarea.send_keys("Eu quero ser Facilitador")

    # Clique no botão de enviar usando JavaScript
    enviar_button = browser.find_element(By.XPATH, "//button[@type='submit']/p[contains(text(), 'Enviar')]")
    browser.execute_script("arguments[0].click();", enviar_button)

    # Aguarda um tempo maior para visualizar o resultado
    time.sleep(20)  # Aumentado para 20 segundos

    # Exibe o título da página acessada após o envio
    print("Título da página após envio:", browser.title)

    # Mantém o navegador aberto para interação manual ou outros fins
    while True:
        time.sleep(60)  # Mantém o navegador aberto indefinidamente

except Exception as ex:
    print(f"Ocorreu um erro: {ex}")

# Finalmente, não fechamos o navegador aqui para mantê-lo aberto
