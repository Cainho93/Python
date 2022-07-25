from random import randint

def lancar_dados():
    return randint(2, 12)

entrada = ''
jogada = ponto = consecutivas = 0


while True:
    print('~' * 80)
    entrada = str(input('Digite "S" para finalizar o programa ou pressione <enter> para iniciar: ')).upper()
    print('~' * 80)
    if entrada == 'S':
        break
    else:
        jogada += 1
        print('=' * 60)
        print(f'Iniciando a {jogada}ª rodada')
        print('=' * 60)
        num = lancar_dados()
        if jogada == 1:
            print(f'Você tirou o número {num}')
            if num == 7 or num == 11:
                print(' "NATURAL", \033[1;32mVocê Ganhou!\033[m')
                consecutivas += 1
            elif num == 2 or num == 3 or num == 12:
                print(' "CRAPS", \033[1;31mVocê Perdeu!\033[m')
                print('=' * 60)
                break
            else:
                ponto = num
                print(f'Sua pontuação é {ponto}')
            print('=' * 60)
        elif jogada > 1:
            print(f'Você tirou o número {num}')
            print(f'Sua pontuação é {ponto}')
            if num == ponto:
                print(f'Você tirou seu ponto que é {ponto}, \033[1;32mVocê Ganhou!\033[m')
                consecutivas += 1
            elif num == 7:
                print('Voce tirou 7 antes de repetir seu ponto, \033[1;31mVocê Perdeu!\033[m')
                print('=' * 60)
                break
            print('=' * 60)
print(f'Você conseguiu {consecutivas} vitórias consecutivas')