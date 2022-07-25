valores = []
maior = menor = 0

for cont in range(0, 5):
    valores.append(int(input(f'Digite um valor na posição {cont}: ')))
    if cont == 0:
        maior = menor = valores[cont]
    else:
        if valores[cont] > maior:
            maior = valores[cont]
        if valores[cont] < menor:
            menor = valores[cont]
print('-=' * 20)
print(f'Os números digitados foram: {valores}')
print(f'O maior valor mostrado foi o {maior} nas posições ', end = '')
for i, v in enumerate(valores):
    if v == maior:
        print(f'{i}... ', end = '')
print('')
print(f'O menor valor mostrado foi o {menor} nas posições ', end = '')
for i, v in enumerate(valores):
      if v == menor:
            print(f'{i}... ', end = '')