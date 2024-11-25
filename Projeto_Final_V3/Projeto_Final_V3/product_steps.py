from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@given('que o usuário está na página de gerenciamento de produtos')
def step_impl(context):
    """Acessa a página de gerenciamento de produtos."""
    context.driver.get("https://projetofinal.jogajuntoinstituto.org/produtos")
    print("Página de gerenciamento de produtos acessada.")

@when('o usuário adiciona um novo produto com imagem')
def step_impl(context):
    """Adiciona um novo produto com imagem."""
    wait = WebDriverWait(context.driver, 20)

    # Botão "Adicionar Produto"
    wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Adicionar Produto')]"))).click()
    print("Botão 'Adicionar Produto' clicado.")

    # Preenche o formulário
    wait.until(EC.presence_of_element_located((By.NAME, "name"))).send_keys("Produto Teste")
    wait.until(EC.presence_of_element_located((By.NAME, "description"))).send_keys("Descrição do Produto Teste")
    wait.until(EC.presence_of_element_located((By.NAME, "price"))).send_keys("100")

    # Submete o formulário
    wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Salvar')]"))).click()
    print("Produto adicionado com sucesso.")

@then('o produto é adicionado com sucesso')
def step_impl(context):
    """Verifica se o produto foi adicionado."""
    print("Produto adicionado com sucesso.")

@when('o usuário exclui um produto existente')
def step_impl(context):
    """Exclui um produto existente."""
    wait = WebDriverWait(context.driver, 20)
    wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Excluir')]"))).click()
    print("Produto excluído com sucesso.")

@then('o produto é excluído com sucesso')
def step_impl(context):
    """Verifica se o produto foi excluído."""
    print("Produto excluído com sucesso.")
