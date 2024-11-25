Feature: Contato com o Instituto Joga Junto
  Como participante do programa Ilhabela Tech
  Quero enviar uma mensagem pelo formulário de contato do site
  Para me candidatar como facilitador

  Scenario: Enviar mensagem com sucesso
    Dado que o usuário acessa a página de contato do Instituto Joga Junto
    Quando o usuário preenche o formulário com seus dados
    Então a mensagem é enviada com sucesso
