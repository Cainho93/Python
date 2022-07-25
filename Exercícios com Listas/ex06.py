medias = list()

for aluno in range(10):
    soma_notas = 0
    print(f'Notas do {aluno + 1}º aluno:')
    print('-' * 20)
    for nota in range(4):
        soma_notas += float(input(f'{nota + 1}ª nota: '))
        medias.append(soma_notas / 4)
        print()
aprovados = 0
for media in medias:
    if media >= 7:
        aprovados += 1
print(f'{aprovados} aluno(s) ficaram com média igual ou acima de 7')