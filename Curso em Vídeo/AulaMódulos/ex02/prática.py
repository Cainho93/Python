import moeda

num = float(input('Digite o preço: R$ '))
print(f'A metade de {moeda.moeda(num)} é {moeda.moeda(moeda.metade(num))}')
print(f'O dobro de {moeda.moeda(num)} é {moeda.moeda(moeda.dobrar(num))}')
print(f'Aumentado em 23% {moeda.moeda(num)}, temos {moeda.moeda(moeda.aumentar(num, 23))}')
print(f'Reduzindo em 45% {moeda.moeda(num)}, temos {moeda.moeda(moeda.diminuir(num, 45))}')