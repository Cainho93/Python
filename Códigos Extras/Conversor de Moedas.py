# Conversor de moedas
from time import sleep
print('=' * 30)
print('{:^30}'.format('CONVERSOR DE MOEDAS'))
print('=' * 30)
while True:
    print('''
______________________

[ 1 ] Real -> Dólar
[ 2 ] Real -> Euro
[ 3 ] Dólar -> Real
[ 4 ] Dólar -> Euro
[ 5 ] Euro -> Real
[ 6 ] Euro -> Dólar
[ 7 ] Sair do programa
______________________
''')
    print('-' * 30)
    conversao = int(input('Digite sua opção de conversão: '))
    while conversao > 7:
        conversao = int(input('Digite sua opção de conversão: '))
    print('')
    if conversao >= 1 and conversao <= 6:
        valor = float(input('Valor para conversão: $ '))
    print('-' * 30)
    print('')
    if conversao == 1:
        moeda = valor / 5.67
        print('R$ {} -> U$ {:.2f}'.format(valor, moeda))
    if conversao == 2:
        moeda = valor / 6.70
        print('R$ {} -> €$ {:.2f}'.format(valor, moeda))
    if conversao == 3:
        moeda = valor * 5.67
        print('U$ {} -> R$ {:.2f}'.format(valor, moeda))
    if conversao == 4:
        moeda = valor * 0.85
        print('U$ {} -> €$ {:.2f}'.format(valor, moeda))
    if conversao == 5:
        moeda = valor * 6.70
        print('€$ {} -> R$ {:.2f}'.format(valor, moeda))
    if conversao == 6:
        moeda = valor / 0.85
        print('€$ {} -> U$ {:.2f}'.format(valor, moeda))
    if conversao == 7:
        break
print('FINALIZANDO PROGRAMA', end = '')
sleep(0.6)
print('.', end = '')
sleep(0.6)
print('.', end = '')
sleep(0.6)
print('.')
sleep(1)
print('PROGRAMA FINALIZADO')