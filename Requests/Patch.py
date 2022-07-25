import requests 

# Editar informação
informacoes = '{"Nome": "Pietro", "Sobrenome": "Faccioni", "Idade": "10"}'
requisicao = requests.patch('https://primeiroprojeto-73648-default-rtdb.firebaseio.com/-Mu8jfghRtsQ3rZ8ZBaR.json', data = informacoes)
print(requisicao)
print(requisicao.json())