from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import logging

# Configuração de logging
logging.basicConfig(level=logging.INFO, format="%(message)s")
logger = logging.getLogger()

def setup_driver():
    """Inicializa o WebDriver do Chrome."""
    try:
        options = Options()
        options.add_argument("--start-maximized")
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=options)
        logger.info("Navegador configurado com sucesso.")
        return driver
    except Exception as e:
        logger.error(f"Erro ao configurar o navegador: {e}")
        raise

def aceitar_cookies(driver):
    """Verifica e aceita cookies, se o pop-up estiver presente."""
    try:
        cookies_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Aceitar')]"))
        )
        cookies_button.click()
        logger.info("Cookies aceitos com sucesso.")
    except Exception:
        logger.info("Pop-up de cookies não encontrado. Continuando.")

def enviar_mensagem():
    """Automatiza o envio de mensagem pelo formulário de contato."""
    try:
        driver = setup_driver()
        driver.get("https://www.jogajuntoinstituto.org/#Contato")
        logger.info("Página carregada com sucesso!")

        # Aceitar cookies
        aceitar_cookies(driver)

        wait = WebDriverWait(driver, 30)

        # Preenche o campo Nome
        nome_input = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div[2]/section[8]/div[1]/form/div[1]/input")))
        nome_input.send_keys("Dione Braga Ferreira")
        logger.info("Campo 'Nome' preenchido.")

        # Preenche o campo E-mail
        email_input = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div[2]/section[8]/div[1]/form/div[2]/input")))
        email_input.send_keys("dionebraga.work@gmail.com")
        logger.info("Campo 'E-mail' preenchido.")

        # Preenche o campo Assunto
        assunto_select = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div[2]/section[8]/div[1]/form/div[3]/select")))
        assunto_select.send_keys("Facilitador Ilhabela Tech")
        logger.info("Campo 'Assunto' preenchido.")

        # Preenche o campo Mensagem
        mensagem_textarea = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div[2]/section[8]/div[1]/form/div[4]/textarea")))
        mensagem = """
        Olá, meu nome é Dione Braga Ferreira, participante do programa Ilhabela Tech. Gostaria de me candidatar para atuar como Facilitador no projeto Joga Junto Instituto.
        Estou à disposição para conversar e esclarecer qualquer dúvida.
        Obrigado!
        """
        mensagem_textarea.send_keys(mensagem)
        logger.info("Campo 'Mensagem' preenchido.")

        # Clique no botão Enviar
        enviar_button = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[2]/section[8]/div[1]/form/div[5]/button")))
        enviar_button.click()
        logger.info("Botão 'Enviar' clicado.")

        # Lidar com o alerta
        try:
            alert = WebDriverWait(driver, 10).until(EC.alert_is_present())
            logger.info(f"Alerta exibido: {alert.text}")
            alert.accept()
            logger.info("Alerta aceito com sucesso.")
        except Exception as e:
            logger.error(f"Erro ao lidar com o alerta: {e}")

        # Mantém o navegador aberto para verificação manual
        input("Pressione Enter para fechar o navegador...")
        driver.quit()

    except Exception as e:
        logger.error(f"Erro ao executar o teste: {e}")
        raise

if __name__ == "__main__":
    enviar_mensagem()
