total = totmil = menor = cont = 0
barato = ''
while True:
    produto = str(input('Nome do produto: ')).lower()
    preco = float(input('Preço: R$ '))
    total += preco
    cont += 1
    if cont == 1 or preco < menor:
        menor = preco
        barato = produto
    if preco > 1000:
        totmil += 1
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar [S/N]: ')).strip().upper()[0]
    if continuar == 'N':
        break
print('{:-^40}'.format(' FIM DO PROGRAMA '))
print(f'O total da compra foi de R$ {total:.2f}')
print(f'Temos {totmil} produtos com o valor acima de R$ 1000')
print(f'O nome do produto mais barato é {barato}')