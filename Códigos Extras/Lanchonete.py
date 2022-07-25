from os import system
from time import sleep
from tabulate import tabulate

# Código  /  Produto  /  Preço  /  Estoque
comidas = [
    [100, 'Carne', 50, 130],
    [200, 'Ataque Culinário', 65, 90],
    [300, 'Cozido Volcano', 100, 110],
    [400, 'Takoyaki', 28, 80],
    [500, 'Onigiri', 39, 120]
]

bebidas = [
    [111, 'Cola', 40, 200],
    [222, 'Saquê', 75, 120],
    [333, 'Jerez', 80, 70],
    [444, 'Rum', 67, 90],
    [555, 'Déesse', 95, 100]
]

lista_comida = []
lista_bebida = []
lista_codigo_comida = [100, 200, 300, 400, 500]
lista_codigo_bebida = [111, 222, 333, 444, 555]
preco_comida = preco_bebida = 0
total_comida = total_bebida = total = 0


while True:
    print('''
    [ 1 ] Comidas
    [ 2 ] Bebidas 
    [ 3 ] Nota Fiscal
    ''')
    opcao = int(input('Selecione sua opção: '))
    while opcao > 3:
        opcao = int(input('Selecione sua opção: '))
    while opcao == 1:
        print(tabulate(comidas, headers = ["CO.", "NOME", "BELLYS ฿", "ESTOQUE"]))
        codigo_comida = int(input('Código ( 0 para o menu ): '))
        while codigo_comida not in lista_codigo_comida:
            codigo_comida = int(input('Código ( 0 para menu ): '))
        if codigo_comida == 0:
            break
        quantidade = int(input('Quantidade: '))
        while quantidade <= 0:
            quantidade = int(input('Quantidade: '))
        for comida in comidas:
            if codigo_comida in comida:
                if comida[3] > quantidade:
                    preco_comida = quantidade * comida[2]
                    lista_comida.append(f'''
                    Pedido: {comida[1]}
                    Quantidade: {quantidade}''')
                    comida[3] = comida[3] - quantidade
                elif comida[3] == 1:
                    print('Desculpe mas o estoque acabou!')
                elif comida[3] <= quantidade:
                    print('Sem chance de venda!')
                break

        total_comida = total_comida + preco_comida
        
    while opcao == 2:
        print(tabulate(bebidas, headers = ["CO.", "NOME", "BELLYS ฿", "ESTOQUE"]))
        codigo_bebida = int(input('Código ( 0 para o menu ): '))
        if codigo_bebida == 0:
            break
        else:
            while codigo_bebida not in lista_codigo_bebida:
                codigo_bebida = int(input('Código ( 0 para menu ): '))
        quantidade = int(input('Quantidade: '))
        while quantidade <= 0:
            quantidade = int(input('Quantidade: '))
        for bebida in bebidas:
            if codigo_bebida in bebida:
                if bebida[3] > quantidade:
                    preco_bebida = quantidade * bebida[2]
                    lista_bebida.append(f'''
                    Pedido: {bebida[1]}
                    Quantidade: {quantidade}''')
                    bebida[3] = bebida[3] - quantidade
                elif bebida[3] == 1:
                    print('Desculpe mas o estoque acabou!')
                elif bebida[3] <= quantidade:
                    print('Sem chance de venda!')
                break

        total_bebida = total_bebida + preco_bebida
    #system('cls')
    if opcao == 3:
        for pedido in lista_comida:
            print(pedido)
        for pedido in lista_bebida:
            print(pedido)       
        print(f'TOTAL TUDO: {total_comida + total_bebida}')
        break
