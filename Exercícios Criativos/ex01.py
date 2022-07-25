# Jogo do par ou ímpar
# Primeiro jogaremos com a maquina, e depois iremos implementar um player vs player
# Criar uma instrução do jogo
from random import randint
from time import sleep

escolha = 0

while escolha != 3:
        # Introdução do jogo ( Menu principal )    
        print('''
    \033[1mJOGO DO PAR OU ÍMPAR\033[m
            
    [ 1 ] Jogador vs Computador
    [ 2 ] Alexa vs Siri
    [ 3 ] Sair do jogo
    ''')
        escolha = int(input('Qual a sua escolha?: '))
        
    # Seleção das modalidades
        # Jogador vs Computador
        while escolha == 1:
            computador = randint(1, 10)
            # Escolhas de número e de par ou ímpar
            # Escolhendo um número superior a 10 voltamos ao menu 
            print('=' * 30)
            jogador = int(input('Escolha um número de 0 à 10: '))
            if jogador > 10:
                break
            total = computador + jogador
            par_ou_impar = str(input('Par ou Ímpar [P/I]: ')).strip().upper()[0]
            # Verificando se o usuário vai escolher certo o par ou ímpar 
            while par_ou_impar not in 'PI':
                par_ou_impar = str(input('Par ou Ímpar [P/I]: ')).strip().upper()[0]
            print('=' * 30)
            
            # Criando um "Loanding"
            print('-' * 15)
            print('RESULTADO', end = '')
            sleep(0.8)
            print('.', end = '')
            sleep(0.6)
            print('.', end = '')
            sleep(0.6)
            print('.')
            print('-' * 15)
            sleep(0.7)
            
            # Resultado da partida
            print(f'\nO computador jogou {computador} e o jogador jogou {jogador}, o total foi de {total}')
            print('~' * 25)
            if par_ou_impar == 'P':
                if total % 2 == 0:
                    print('\033[1;32mJOGADOR É O VENCEDOR!\033[m')
                    print('~' * 25)
                else:
                    print('\033[1;32mCOMPUTADOR É O VENCEDOR!\033[m')
                    print('~' * 25)
                    break
            elif par_ou_impar == 'I':
                if total % 2 == 1:
                    print('\033[1;32mJOGADOR É O VENCEDOR!\033[m')
                    print('~' * 25)
                else:
                    print('\033[1;32mCOMPUTADOR É O VENCEDOR!\033[m')
                    print('~' * 25)
                    break
            
        # Alexa vs Siri
        while escolha == 2:
            # Variáveis
            alexa = randint(0, 10)
            siri = randint(0, 10)
            total = alexa + siri
            
            # Criando um "Loanding"
            print('-' * 15)
            print('RESULTADO', end = '')
            sleep(0.8)
            print('.', end = '')
            sleep(0.6)
            print('.', end = '')
            sleep(0.6)
            print('.')
            print('-' * 15)
            sleep(0.7)
            # Aviso de quem é quem 
            print('\033[1mLembrando que a ALEXA é PAR e a SIRI é ÍMPAR\033[m')
            sleep(1)
            
            # Resultado da partida
            print(f'\nA ALEXA jogou {alexa} e a SIRI jogou {siri}, o total foi de {total}')
            print('~' * 20)
            if total % 2 == 0:
                print('\033[1;32mALEXA É A VENCEDORA!\033[m')
                print('~' * 20)
                break
            else:
                print('\033[1;32mSIRI É A VENCEDORA!\033[m')
                print('~' * 20)
                break