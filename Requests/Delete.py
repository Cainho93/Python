import requests 

# Deletar informação
requisicao = requests.delete('https://primeiroprojeto-73648-default-rtdb.firebaseio.com/-Mu8jfghRtsQ3rZ8ZBaR.json')
print(requisicao)
print(requisicao.json())