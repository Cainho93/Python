tot_maioridade = tot_homem = tot_mulher20 = 0
while True:
    print('=' * 20)
    print('CADASTRE UMA PESSOA')
    print('=' * 20)
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo [M/F]: ')).strip().upper()[0]
    if idade > 18:
        tot_maioridade += 1
    if sexo == 'M':
        tot_homem += 1
    if sexo == 'F' and idade < 20:
        tot_mulher20 += 1
    continuar = ' '
    while continuar not in 'SN':
        print('~' * 20)
        continuar = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
        print('~' * 20)
    if continuar == 'N':
        break
print(f'Foram cadastradas {tot_maioridade} pessoas maiores de 18 anos')
print(f'Foram cadastrados {tot_homem} homens')
print(f'Foram cadastradas {tot_mulher20} mulheres menores de 20 anos')