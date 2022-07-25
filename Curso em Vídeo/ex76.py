listagem = ('Tesoura', 3.65, 
            'Caneta', 7.50, 
            'Mochila', 50,
            'Lápis', 2,
            'Caderno', 32.75,
            'Estojo', 10, 
            'Transferidor', 12.89, 
            'Compasso', 15)
print('=' * 40)
print('{:^40}'.format('TABELA DE PREÇOS'))
print('=' * 40)
print('')
for pos in range(0, len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<30}', end = '')
    if pos % 2 == 1:
        print(f'R${listagem[pos]:>7.2f}')