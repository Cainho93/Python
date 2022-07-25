soma = maior = menor = quant = 0
while True:
    num = int(input('Informe um valor: '))
    while num > 1000:
        num = int(input('Informe um valor até 1000: '))
    soma += num
    quant += 1
    if quant == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    resp = str(input('Quer continuar [S/N]: ')).strip().upper()[0]
    while resp not in 'SN':
        resp = str(input('Quer continuar [S/N]: ')).strip().upper()[0]
    if resp in 'N':
        break
print('-' * 30)
print(f'Menor valor: {menor}')
print(f'Maior valor: {maior}')
print(f'Soma de todos os valores: {soma}')