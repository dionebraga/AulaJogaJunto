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
    """Configura o WebDriver do Chrome."""
    options = Options()
    options.add_argument("--start-maximized")
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    return driver

def enviar_mensagem():
    """Automatiza o envio de mensagem pelo formulário de contato."""
    driver = setup_driver()
    try:
        # Acesse o site
        driver.get("https://www.jogajuntoinstituto.org/#Contato")
        logger.info("Site acessado com sucesso.")

        wait = WebDriverWait(driver, 30)  # Aumentando o tempo de espera para carregar os elementos

        # Preencha o campo Nome
        nome = wait.until(EC.presence_of_element_located((By.NAME, "your-name")))
        nome.clear()
        nome.send_keys("Dione Braga Ferreira")
        logger.info("Campo 'Nome' preenchido.")

        # Preencha o campo E-mail
        email = wait.until(EC.presence_of_element_located((By.NAME, "your-email")))
        email.clear()
        email.send_keys("dionebraga.work@gmail.com")
        logger.info("Campo 'E-mail' preenchido.")

        # Preencha o campo Assunto
        assunto = wait.until(EC.presence_of_element_located((By.NAME, "your-subject")))
        assunto.clear()
        assunto.send_keys("Facilitador Ilhabela Tech")
        logger.info("Campo 'Assunto' preenchido.")

        # Preencha o campo Mensagem
        mensagem = """
        Olá, meu nome é Dione Braga Ferreira, participante do programa Ilhabela Tech. Gostaria de me candidatar para atuar como Facilitador no projeto Joga Junto Instituto. 
        Estou à disposição para conversar e esclarecer qualquer dúvida.
        Obrigado!
        """
        mensagem_box = wait.until(EC.presence_of_element_located((By.NAME, "your-message")))
        mensagem_box.clear()
        mensagem_box.send_keys(mensagem)
        logger.info("Campo 'Mensagem' preenchido.")

        # Clique no botão Enviar
        enviar_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@value='Enviar']")))
        enviar_button.click()
        logger.info("Mensagem enviada com sucesso.")

    except Exception as e:
        logger.error(f"Erro ao enviar a mensagem: {e}")
    finally:
        logger.info("Finalizando o teste...")
        # Manter o navegador aberto para inspeção
        input("Pressione Enter para fechar o navegador...")
        driver.quit()

# Executa a função
if __name__ == "__main__":
    enviar_mensagem()
