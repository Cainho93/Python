litros = int(input('Quantos litros de combustível: '))
tipo = str(input('É Gasolina ou Álcool [G/A]?: ')).strip().upper()[0]
preco =  desconto = 0
if tipo in 'A':
    alcool = 1.90
    preco = alcool * litros
    if litros <= 20:
        desconto = preco - (preco * 3 / 100)
    elif litros > 20:
        desconto = preco - (preco * 5 / 100)
elif tipo in 'G':
    gasolina = 2.50
    preco = gasolina * litros
    if litros <= 20:
        desconto = preco - (preco * 4 / 100)
    elif litros > 20:
        desconto = preco - (preco * 6 / 100)
else:
    print('Tipo de combustível INVÁLIDO.')
print('-' * 35)    
print(f'O preço à pagar será de R${desconto:.2f}')