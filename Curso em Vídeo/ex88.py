from random import randint
from time import sleep
print('-' * 30)
print('{:^30}'.format('JOGO DA MEGA SENA'))
print('-' * 30)
lista = list()
jogos = list()
tot = 1
quant = int(input('Quantos jogos quer fazer: '))
print()
while tot <= quant:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
print('-=' * 3, f'SORTEANDO {quant} JOGOS', '-=' * 3)
for i, j in enumerate(jogos):
    print(f'Jogo {i + 1}: {j}')
    sleep(1)
print('-=' * 5, 'BOA SORTE', '-=' * 5)