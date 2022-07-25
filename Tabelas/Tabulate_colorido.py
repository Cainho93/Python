from tabulate import tabulate
from termcolor import colored

def criar_cabecalho():
    cabecalho = ['Times', 'Paulistão', 'Brasileirão', 'Copa do Brasil']
    return [colored(c, 'cyan', attrs = ['bold']) for c in cabecalho]

def criar_tabela():
    tabela = [
        ['Corinthians', 30, 7, 3],
        ['Palmeiras', 23, 10, 4],
        ['Santos', 22, 8, 3],
        ['São Paulo', 22, 6, 0]
    ] 
    return [
        [colored(d[0], 'yellow', attrs = ['bold']), d[1], d[2], d[3]] for d in tabela
    ]
    
print(tabulate(criar_tabela(), headers = criar_cabecalho(), tablefmt = 'fancy_grid'))