import requests

link = 'https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL'

req = requests.get(link)
req = req.json()
cot_dol = req['USDBRL']['bid']
# O :.(algum número) serve para delimitar quantos numeros haverão no total
# OBS: O (.) conta, ent se vc quiser 2 numeros após o (. ou ,) coloque o 4 como parametro 
print(f'Essa é a cotação do Dólar: US {cot_dol:.4}')