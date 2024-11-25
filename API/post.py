import requests
from faker import Faker

fake = Faker('pt_BR')

url_api ='https://fakerestapi.azurewebsites.net/api/v1/Authors'

headers = {
    'Accept': '*/*',
    'User-Agent': 'requests'  
}
novo_autor = {
  "id": 0,
  "idBook": 0,
  "firstName": fake.name(),
   "lastName": fake.last_name()
}
resposta = requests.post(url_api, headers=headers, json = novo_autor)
resposta_dict = resposta.json()
print(resposta_dict)
if resposta.status_code == 200:
    print(f"Autor criado")  
else: 
    print("Não foi possível criar autor")