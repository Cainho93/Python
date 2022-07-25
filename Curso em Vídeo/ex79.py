num = list()

while True:
    n = int(input('Digite um valor: '))
    if n not in num:
        num.append(n)
        print('Valor adicionado...')
    else:
        print('Valor duplicado... Não adicionado')
    r = str(input('Quer continuar: [S/N] ')).strip().upper()[0]
    while r not in 'SN':
        r = str(input('Quer continuar: [S/N] ')).strip().upper()[0]
    if r == 'N':
        break
print('-=' * 26)
num.sort()
print(f'Lista em ordem crescente: {num}')