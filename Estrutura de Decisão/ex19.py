kg_maca = int(input('Quantos Kg de maçã você gostaria: '))
kg_morango = int(input('Quantos Kg de morango você gostaria: '))

maca = morango = total = kg_total = desconto = 0

if kg_maca <= 5:
    maca = kg_maca * 1.80
else:
    maca = kg_maca * 1.50

if kg_morango <= 5:
    morango = kg_morango * 2.50
else:
    morango = kg_morango * 2.20

kg_total = kg_maca + kg_morango
total = maca + morango

if kg_total > 8 or total > 25:
    desconto = total - (total * 10 / 100)
    print(f'O preço à se pagar é de R${desconto:.2f}')
else:
    total = total
    print(f'O preço à se pagar é de R${total:.2f}')