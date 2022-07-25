import moeda

num = float(input('Digite o preço: R$ '))
print(f'A metade de R$ {num} é R$ {moeda.metade(num)}')
print(f'O dobro de R$ {num} é R$ {moeda.dobrar(num)}')
print(f'Aumentado em 30% R$ {num}, temos {moeda.aumentar(num, 30)}')