n1 = int(input('Informe o 1º valor: '))
n2 = int(input('Informe o 2º valor: '))
n3 = int(input('Informe o 3º valor: '))
maior = 0
if n1 > n2 and n1 > n3:
    maior = n1
elif n2 > n1 and n2 > n3:
    maior = n2
else:
    maior = n3
menor = 0
if n1 < n2 and n1 < n3:
    menor = n1
elif n2 < n1 and n2 < n3:
    menor = n2
else:
    menor = n3
print('-' * 24)    
print(f'O MAIOR número é o {maior}')
print(f'O MENOR número é o {menor}')