num = list()
pares = []
impares = list()
while True:
    num.append(int(input('Digite um valor: ')))
    resp = str(input('Quer continuar [S/N] ')).strip().upper()[0]
    while resp not in 'SN':
        resp = str(input('Quer continuar [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print('-=' * 26)
print(f'Lista completa: {num}')
for n in num:
    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)
print(f'Lista dos PARES: {pares}')
print(f'Lista dos ÍMPARES: {impares}')