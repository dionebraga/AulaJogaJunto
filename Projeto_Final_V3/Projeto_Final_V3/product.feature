Feature: Gerenciamento de Produtos
  Como administrador do sistema
  Quero adicionar e excluir produtos
  Para gerenciar o estoque eficientemente

  Scenario: Adicionar um novo produto com imagem
    Dado que o usuário está na página de gerenciamento de produtos
    Quando o usuário adiciona um novo produto com imagem
    Então o produto é adicionado com sucesso

  Scenario: Excluir um produto existente
    Dado que o usuário está na página de gerenciamento de produtos
    Quando o usuário exclui um produto existente
    Então o produto é excluído com sucesso
