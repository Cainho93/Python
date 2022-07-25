from random import randint
print('Sou seu computador...\nAcabei de pensar em um número entre 0 e 10')
print('Será que você consegue adivinhar qual foi?')
print('')
computador = randint(0, 10)
acertou = False
tentativas = 0
while not acertou:
    jogador = int(input('Chute um número: '))
    tentativas += 1
    if jogador == computador:
        acertou = True
    if jogador > computador:
        print('Menos... Tente novamente.')
    if jogador < computador:
        print('Mais... Tente novamente.')
print('Acertou em {} tentativas. PARABÉNS!'.format(tentativas))