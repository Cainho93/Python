from tabulate import tabulate 

cabecalho = ['Times', 'Paulistão', 'Brasileirão', 'Copa do Brasil']
tabela = [
    ['Corinthians', 30, 7, 3],
    ['Palmeiras', 23, 10, 4],
    ['Santos', 22, 8, 3],
    ['São Paulo', 22, 6, 0]
]

print(tabulate(tabela, headers = cabecalho, tablefmt = 'fancy_grid'))