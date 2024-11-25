import requests

url_api ='https://fakerestapi.azurewebsites.net/api/v1/Authors/'

headers = {
    'Accept': '*/*',
    'User-Agent': 'requests'  
}

resposta = requests.get(url_api, headers=headers)

if resposta.status_code == 200:
    print(f"API Funcionando")  
else:
    print(f"Erro ao acessar a API: {resposta.status_code}")
    print(resposta.text) 
#Procurano nome dos autores na API
resposta_json = resposta.json()
if resposta_json:  # Se a lista não estiver vazia
        for author in resposta_json:
            print(f"Nome: {author['firstName']} {author['lastName']}")  
else:
     print (f"Lista Vazia")
  