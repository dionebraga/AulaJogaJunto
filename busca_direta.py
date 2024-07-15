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
    # Link da página de contato
    link_contato = "https://www.jogajuntoinstituto.org/#Contato"

    # Abre a página de contato
    browser.get(link_contato)

    # Espera a página carregar completamente
    time.sleep(5)  # Aumentado para 5 segundos

    # Scroll até o formulário de contato
    formulario_contato = browser.find_element(By.ID, "Contato")
    browser.execute_script("arguments[0].scrollIntoView(true);", formulario_contato)

    # Preenche os campos
    nome_input = browser.find_element(By.ID, "nome")
    nome_input.send_keys("Dione Braga")

    email_input = browser.find_element(By.ID, "email")
    email_input.send_keys("dionebraga.work@gmail.com")

    assunto_select = browser.find_element(By.ID, "assunto")
    assunto_select.send_keys("Ser facilitador")  # Seleciona o assunto desejado

    mensagem_textarea = browser.find_element(By.ID, "mensagem")
    mensagem_textarea.send_keys("Eu quero ser Facilitador")

    # Clique no botão de enviar
    enviar_button = browser.find_element(By.XPATH, "//button[@type='submit']/p[contains(text(), 'Enviar')]")
    browser.execute_script("arguments[0].click();", enviar_button)

    # Aguarda um tempo maior para visualizar o resultado
    time.sleep(15)  # Aumentado para 15 segundos

    # Exibe o título da página acessada
    print("Título da página:", browser.title)

    # Mantém o navegador aberto para interação manual
    input("Pressione Enter para fechar o navegador apenas quando desejar...")

except Exception as ex:
    print(f"Ocorreu um erro: {ex}")

# Finalmente, não fechamos o navegador aqui para mantê-lo aberto
