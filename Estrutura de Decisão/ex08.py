p1 = float(input('Informe o valor do 1º produto: R$ '))
p2 = float(input('Informe o valor do 2º produto: R$ '))
p3 = float(input('Informe o valor do 3º produto: R$ '))

menor_preco = 0

if p1 < p2 and p1 < p3:
    menor_preco = p1
elif p2 < p1 and p2 < p3:
    menor_preco = p2
else:
    menor_preco = p3
print('\nA escolha de compra será do produto mais em conta.')
print(f'O produto que está mais barato e que será levado pelo cliente é o que custa R$ {menor_preco:.2f}')