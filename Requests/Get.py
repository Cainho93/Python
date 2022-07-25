import requests 

# Adicionar informação
requisicao = requests.get(' https://primeiroprojeto-73648-default-rtdb.firebaseio.com/.json')
print(requisicao)
print(requisicao.json())