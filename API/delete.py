import requests

url_api ='https://fakerestapi.azurewebsites.net/api/v1/Authors/'

headers = {
    'Accept': '*/*',
    'User-Agent': 'requests'  
}
post_id = 12
resposta = requests.delete(url_api + str(post_id), headers=headers)

if resposta.status_code == 200:
    print("Autor deletado com sucesso.")