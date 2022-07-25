# Habilidades praticas a aplicar:

# Tratamento de exceções
# Condicionais If/Else
# Input de dados
# Geração de valores
# Print

# Gere um número aleatório de 1 à 6

from random import randint

while True:
    try:
        print()
        resp = str(input('Quer jogar o dado? [S/N]: ')).strip().upper()[0]
    except IndexError:
        print('Você \033[1;31mNÃO\033[m pode pressionar ENTER responda com [S/N]')
    except KeyboardInterrupt:
        print('O usuário \033[1;31mNÃO\033[m pode encerrar o programa desse jeito.')
    else:
        if resp == 'S':
            num = randint(1, 6)
            print(f'''
  ==================================         
         SIMULADOR DE DADOS
            
    O número dado pelo dado foi \033[1m{num}\033[m
  ================================== ''')
        elif resp == 'N':
            print('FIM DO PROGRAMA.')
            break