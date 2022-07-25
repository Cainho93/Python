maior = 0
for n in range(5):
    num = int(input('Informe um número inteiro: '))
    if n == 1:
        maior = num
    else:
        if num > maior:
            maior = num
print(f'O maior número é o {maior}')