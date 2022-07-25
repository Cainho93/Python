pessoa = dict()
grupo = list()
somaidade = 0
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: '))
    pessoa['sexo'] = str(input('Sexo [M/F] ')).upper().strip()[0]
    while pessoa['sexo'] not in 'MF':
        pessoa['sexo'] = str(input('Sexo [M/F] ')).upper().strip()[0]
    pessoa['idade'] = int(input('Idade: '))
    somaidade += pessoa['idade']
    grupo.append(pessoa.copy())
    resp = str(input('Continuar [S/N] ')).strip().upper()[0]
    while resp not in 'SN':
        resp = str(input('Continuar [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print('-=' * 30)
print(f'- O grupo tem {len(grupo)} pessoas')
media = somaidade / len(grupo)
print(f'- A média de idade do grupo é {media:.2f}')
print('- As mulheres cadastradas foram ', end = '')
for p in grupo:
    if p['sexo'] in 'F':
        print(f'[{p["nome"]}] ', end = '')
print()
print('- Lista das pessoas que estão acima da média:')
for p in grupo:
    if p['idade'] >= media:
        print('    ')
        for k, v in p.items():
            print(f'{k} = {v}; ', end = '')
        print()