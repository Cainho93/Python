import requests

url = 'https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol=IBM&apikey=582XS47GZBXC9DPE'
r = requests.get(url)
data = r.json()
print(data)