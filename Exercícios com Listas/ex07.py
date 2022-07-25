num = []
p = 1
for n in range(5):
    num.append(int(input('Informe um valor: ')))
for n in num:
    p *= n
print('-' * 20)
print(f'A soma entre os valores é {sum(num)}')
print(f'A multiplicação entre os valores é {p}')