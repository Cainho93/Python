ficha = dict()

ficha['nome'] = str(input('Nome: '))
ficha['média'] = float(input(f'Média de {ficha["nome"].capitalize()}: '))
if ficha['média'] >= 7:
    ficha['situação'] = 'Aprovado'
elif 5 <= ficha['média'] < 7:
    ficha['situação'] = 'Recuperação'
else:
    ficha['situação'] = 'Reprovado'
for k, v in ficha.items():
    print(f'{k.capitalize()} é igual a {v}')