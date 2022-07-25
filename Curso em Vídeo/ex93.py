jogador = dict()
gols = list()
gol = tot = 0
jogador['nome'] = str(input('Nome do jogador: '))
partidas = int(input(f'Quantas partidas {jogador["nome"].capitalize()} jogou: '))
for i in range(0, partidas):
    gol = int(input(f'Quantos gols {jogador["nome"].capitalize()} marcou na {i + 1}ª partida?: '))
    tot += gol
    gols.append(gol)
jogador['gols'] = gols
jogador['total'] = tot
print('-=' * 30)
print(jogador)
print('-=' * 30)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print('-=' * 30)
print(f'O jogador {jogador["nome"].capitalize()} jogou {partidas} partidas.')
for p, g in enumerate(gols):
    print(f'  => Na {p + 1}ª partida, fez {g} gols.')
print(f'O total foi de {tot} gols.')
print('-=' * 30)