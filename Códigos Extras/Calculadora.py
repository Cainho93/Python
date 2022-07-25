import math
from time import sleep
a = ('=' * 30)
b = ('<=>' * 10)
print('{:=^40}'.format('CALCULADORA'))
opcao = 0
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
while opcao != 12:
    print('')
    print('''    Opções
    ============================
    [ 1 ] Soma
    [ 2 ] Subtração
    [ 3 ] Multiplicação
    [ 4 ] Divisão
    [ 5 ] Raiz Quadrada
    [ 6 ] Potência
    [ 7 ] Tabuada
    [ 8 ] Par ou Ímpar
    [ 9 ] Conversão para Binário
    [ 10 ]  π
    [ 11 ] Novos números
    [ 12 ] Sair
    ============================
    ''')
    opcao = int(input('Opção: '))
    if opcao == 1:
        print('{} + {} = {}'.format(n1, n2, n1 + n2))
    elif opcao == 2:
        print('{} - {} = {}'.format(n1, n2, n1 - n2))
    elif opcao == 3:
        print('{} x {} = {}'.format(n1, n2, n1 * n2))
    elif opcao == 4:
        print('{} ÷ {} = {}'.format(n1, n2, n1 / n2))
    elif opcao == 5:
        print('√{} = {}\n√{} = {}'.format(n1, math.sqrt(n1), n2, math.sqrt(n2)))
    elif opcao == 6:
        elevado1 = int(input('Elevar a qual potência: '))
        elevado2 = int(input('Elevar a qual potência: '))
        print('{} elevado {} = {}\n{} elevado {} = {}'.format(n1, elevado1, math.pow(n1, elevado1), n2, elevado2, math.pow(n2, elevado2)))
    elif opcao == 7:
        for i in range(1, 11):
            print('{} x {} = {}'.format(n1, i, n1 * i))
        print('==============')
        for c in range(1, 11):
            print('{} x {} = {}'.format(n2, c, n2 * c))
    elif opcao == 8:
        if n1 % 2 == 0:
            print('{}\nPar'.format(n1))
        if n1 % 2 == 1:
            print('{}\nÍmpar'.format(n1))
        if n2 % 2 == 0:
            print('{}\nPar'.format(n2))
        if n2 % 2 == 1:
            print('{}\nÍmpar'.format(n2))
    elif opcao == 9:
        print('{} = {}\n{} = {}'.format(n1, bin(n1)[2:], n2, bin(n2)[2:]))
    elif opcao == 10:
        print(' π = {:.2f}'.format(math.pi))
    elif opcao == 11:
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    elif opcao == 12:
        print('Finalizando', end = '')
        sleep(0.6)
        print('.', end = '')
        sleep(0.6)
        print('.', end = '')
        sleep(0.6)
        print('.')
        sleep(1)
    else:
        print('Opção Inválida!')
print('Fim de programa.')