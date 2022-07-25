from time import sleep
from random import randint
a = ('-=' * 26)
b = ('~' * 21)
computador = randint(0, 10)
print('{:=^41}'.format(' \033[1;34mJOGO DA ADIVINHAÇÃO\033[m '))
print('')
print('''\033[1;41mAVISOS\033[m: O jogador vai escolher um número de 0 à 10\nO computador vai escolher um número de 0 à 10
\nDito isso a graça do jogo é adivinhar a soma da escolha do jogador e do computador''')
print('')
print(a)
jogador = int(input('Digite o valor para somar com o computador: '))
print(a)
soma = jogador + computador
chute = 0
tentativas = 0
while chute != soma:
    print(b)
    chute = int(input('Chute o valor da soma: '))
    tentativas += 1
    if chute < soma:
        print('\033[1;34mMAIS...\033[m')
    if chute > soma:
        print('\033[1;33mMENOS...\033[m')
    if chute == soma:
        print('\033[1;32mACERTOU!!!\033[m')
print(b)
print('Você adivinhou a soma dos números {} + {} em {} tentativas'.format(jogador, computador, tentativas))