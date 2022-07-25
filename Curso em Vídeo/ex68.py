from random import randint
v = 0
print('-=' * 15)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('-=' * 15)
while True:
    jogador = int(input('Digite um número: '))
    computador = randint(0, 10)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Ímpar [P/I]: ')).strip().upper()[0]
        print('-' * 25)
    print(f'Você jogou {jogador} e o cumputador {computador}. O total foi {total}')
    if tipo == 'P':
        if total % 2 == 0:
            print('Você VENCEU!\nVamos jogar novamente...')
            v += 1
        else:
            print('Você PERDEU!')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('Você VENCEU!\nVamos jogar novamente...')
            v += 1
        else:
            print('Você PERDEU!')
            break
print(f'GAME OVER! Você conseguiu {v} vitórias consecutivas')