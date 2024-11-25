Feature: Login no Sistema
  Como administrador do sistema
  Quero fazer login no sistema
  Para gerenciar os produtos

  Scenario: Fazer login com sucesso
    Dado que o usuário acessa a página de login do sistema
    Quando o usuário insere suas credenciais e faz login
    Então o sistema exibe a página inicial
