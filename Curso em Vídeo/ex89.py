from time import sleep
boletim = list()
while True:
    nome = str(input('Nome: '))
    n1 = float(input('Nota 1: '))
    n2 = float(input('Nota 2: '))
    media = (n1 + n2) / 2
    boletim.append([nome, [n1, n2], media])
    r = str(input('Quer continuar [S/N] ')).upper().strip()[0]
    while r not in 'SN':
        r = str(input('Quer continuar [S/N] ')).strip().upper()[0]
    if r == 'N':
        break
print('-=' * 30)
print(f'{"NO.":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-' * 26)
for i, a in enumerate(boletim):
    print(f'{i:<4}{a[0].capitalize():<10}{a[2]:>8.2f}')
print('-' * 26)
while True:
    opc = int(input('NO. para ver nota individual [999 para parar]: '))
    if opc == 999:
        print('-' * 32)
        print('FINALIZANDO', end = '')
        sleep(0.6)
        print('.', end = '')
        sleep(0.6)
        print('.', end = '')
        sleep(0.6)
        print('.')
        print('-' * 32)
        break
    else:
        if opc <= len(boletim) - 1:
            print('-' * 32)
            print(f'Notas de {boletim[opc][0].capitalize()} são {boletim[opc][1]}')
            print('-' * 32)
        if opc > len(boletim) - 1:
            print('-' * 32)
            print('Digite um NO. válido!')
            print('-' * 32)