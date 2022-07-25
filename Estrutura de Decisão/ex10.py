periodo = str(input('Em qual período você estuda [M - Matutino/V - Vespertino/N - Noturno]: ')).strip().upper()[0]

if periodo in 'MVN':
    if periodo == 'M':
        print('Bom dia!')
    if periodo == 'V':
        print('Boa tarde!')
    if periodo == 'N':
        print('Boa noite!')
else:
    print('Período INEXISTENTE!')