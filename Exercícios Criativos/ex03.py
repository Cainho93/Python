from random import randint

# Habilidades praticas a aplicar:

# Random                                                   
# Comparadores matemáticos
# Controle de Fluxo
# Entrada de dados
# Saida de dados

sorteado = randint(0, 20)
while True:
    try:
        chute = int(input('Chute um número: '))
    except ValueError:
        print('Digite \033[1mSOMENTE\033[m números.')
    except KeyboardInterrupt:
        print('O usuário \033[1;31mNÃO\033[m pode encerrar o programa desse jeito.')
    else:
        if chute > sorteado:
            print('\033[1;34mMENOS...\033[m Chute um número menor.')
        elif chute < sorteado:
            print('\033[1;35mMAIS...\033[m Chute um número maior.')
        elif chute == sorteado:
            print('\033[1;32mMEUS PARABÉNS\033[m. Você acertou!')
            break

