time = list()
jogador = dict()
gols = list()
while True:
    jogador.clear()
    jogador['nome'] = str(input('Nome do jogador: '))
    partidas = int(input(f'Quantas partidas {jogador["nome"].capitalize()} jogou: '))
    gols.clear()
    for i in range(0, partidas):
        gols.append(int(input(f'Quantos gols na {i + 1}ª partida?: ')))
    jogador['gols'] = gols[:]
    jogador['total'] = sum(gols)
    time.append(jogador.copy())
    resp = str(input('Continuar [S/N] ')).upper().strip()[0]
    while resp not in 'SN':
        resp = str(input('Continuar [S/N] ')).upper().strip()[0]
    if resp == 'N':
        break
print('-=' * 30)
print('cod ',end = '')
for i in jogador.keys():
    print(f'{i:<17}', end = '')
print()
print('-' * 43)
for k, v in enumerate(time):
    print(f'{k:>3} ', end = '')
    for d in v.values():
        print(f'{str(d):<16} ', end = '')
    print()
print('-' * 43)
while True:
    busca = int(input('COD. para mostrar dados do jogador [999 interromper] '))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'ERRO! Não existe jogador com o COD. {busca}!')
    else:
        print(f' -- LEVANTAMENTO DO JOGADOR {time[busca]["nome"]} -- ')
        for i, g in enumerate(time[busca]['gols']):
            print(f'  No {i + 1}º jogo foram feitos {g} gols ')
print('<< VOLTE SEMPRE >> ')