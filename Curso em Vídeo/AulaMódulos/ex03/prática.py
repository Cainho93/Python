import moeda

num = float(input('Digite o preço: R$ '))
print(f'A metade de {moeda.moeda(num)} é {moeda.metade(num, True)}')
print(f'O dobro de {moeda.moeda(num)} é {moeda.dobrar(num, True)}')
print(f'Aumentado em 23% {moeda.moeda(num)}, temos {moeda.aumentar(num, 23, True)}')
print(f'Reduzindo em 45% {moeda.moeda(num)}, temos {moeda.diminuir(num, 45, True)}')
