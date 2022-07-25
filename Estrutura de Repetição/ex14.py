gabarito = list()
resps_aluno = list()
notas_tiradas = list()
print('\033[1mGabarito\n\033[m')
for i in range(10):
    resp_certa = gabarito.append(str(input(f'{i + 1}ª Questão: ')))
num_aluno = 1
while True:
    print(f'\n\033[1mAluno nº: {num_aluno}\n\033[m')
    resps_aluno.clear()
    for i in range(10):
        resp_aluno = resps_aluno.append(str(input(f'{i + 1}ª Questão: ')))
    nota = 0
    for i in range(10):
        if resps_aluno[i] == gabarito[i]:
            nota += 1
    notas_tiradas.append(nota)
    cont = str(input('Outro aluno vai utilizar o sistema [S/N]: ')).upper().strip()[0]
    while cont not in 'SN':
        cont = str(input('Outro aluno vai utilizar o sistema [S/N]: ')).upper().strip()[0]
    if cont in 'S':
        num_aluno += 1
        continue
    if cont in 'N':
        break
print(f'{len(notas_tiradas)} alunos utilizaram o sistema')
print(f'A maior nota foi: {max(notas_tiradas)}\nA menor nota foi: {min(notas_tiradas)}')
print(f'A média da turma foi de: {sum(notas_tiradas) / len(notas_tiradas)}')
print(notas_tiradas)