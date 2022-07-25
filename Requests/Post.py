import requests
# Quando o método Post é usado você precisa colocar alguma informação
informacoes = '{"Nome": "Andre"}'
requisicao = requests.post('https://primeiroprojeto-73648-default-rtdb.firebaseio.com/.json', data = informacoes)
print(requisicao)
print(requisicao.json())