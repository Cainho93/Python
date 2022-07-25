from random import randint
from time import sleep
from operator import itemgetter
jogadas = dict()
ranking = list()
jogadas['Jogador1'] = randint(1, 6)
jogadas['Jogador2'] = randint(1, 6)
jogadas['Jogador3'] = randint(1, 6)
jogadas['Jogador4'] = randint(1, 6)
print('-' * 28)
for j, d in jogadas.items():
    print(f'O {j} jogou {d} no dado.')
    sleep(1)
print('-' * 28)
print('---- RANKING ----')
ranking = sorted(jogadas.items(), key = itemgetter(1), reverse = True)
for i, v in enumerate(ranking):
    print(f'{i + 1}º lugar: {v[0]} com {v[1]}')
    sleep(1)