num = [[], []]
valor = 0
for cont in range(0, 7):
    valor = int(input(f'Digite o {cont + 1}º valor: '))
    if valor % 2 == 0:
        num[0].append(valor)
    else:
        num[1].append(valor)
print('-=' * 10)
num[0].sort()
print(f'Pares: {num[0]}')
num[1].sort()
print(f'Ímpares: {num[1]}')