sexo = str(input('Sexo [M/F]: ')).strip().upper()[0]
if sexo == 'M':
    print('SEXO MASCULINO')
elif sexo == 'F':
    print('SEXO FEMININO')
else:
    print('SEXO INVÁLIDO')