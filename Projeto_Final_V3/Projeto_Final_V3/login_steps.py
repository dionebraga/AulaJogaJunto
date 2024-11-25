from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import logging

# Configuração de logging
logging.basicConfig(level=logging.INFO, format="%(message)s")
logger = logging.getLogger()

def setup_driver():
    """Inicializa o WebDriver do Chrome."""
    options = Options()
    options.add_argument("--start-maximized")
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    return driver

@given('que o usuário acessa a página de login do sistema')
def step_impl(context):
    """Acessa a página de login."""
    logger.info("Acessando a página de login do sistema...")
    context.driver = setup_driver()
    context.driver.get("https://projetofinal.jogajuntoinstituto.org/")
    logger.info("Página de login acessada.")

@when('o usuário insere suas credenciais e faz login')
def step_impl(context):
    """Realiza o login."""
    email = "dionebraga.work@gmail.com"
    senha = "123456"
    logger.info(f"Inserindo credenciais: {email}")
    try:
        wait = WebDriverWait(context.driver, 20)

        # Campo de e-mail
        wait.until(EC.presence_of_element_located((By.ID, "mui-1"))).send_keys(email)
        logger.info("E-mail preenchido.")

        # Campo de senha
        wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div/main/form/div[2]"))).send_keys(senha)
        logger.info("Senha preenchida.")

        # Botão "Iniciar Sessão"
        wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/main/form/button"))).click()
        logger.info("Botão 'Iniciar Sessão' clicado.")
    except Exception as e:
        logger.error(f"Erro ao realizar login: {e}")
        raise

@then('o sistema exibe a página inicial')
def step_impl(context):
    """Verifica se o login foi bem-sucedido."""
    try:
        wait = WebDriverWait(context.driver, 20)
        wait.until(EC.presence_of_element_located((By.XPATH, "//h1[contains(text(), 'Página Inicial')]")))
        logger.info("Login realizado com sucesso. Página inicial exibida.")
    except Exception as e:
        logger.error(f"Erro ao verificar a página inicial: {e}")
        raise
