import requests
import json

data_inicial = '20210101'
data_final = '20210131'
# Oq vem dps da ? são os parametros que tem ser passados na url, sempre que a API por exemplo pedir
# uma Query, é preciso saber que os parametros vem dps da ? 
link = f'https://economia.awesomeapi.com.br/json/daily/USD-BRL/?start_date={data_inicial}&end_date={data_final}'

requisicao = requests.get(link)
teste = json.loads(requisicao.content)
print('=' * 35)
print(teste[0]['name'])
print('=' * 35)
