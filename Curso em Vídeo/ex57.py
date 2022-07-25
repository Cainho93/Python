sexo = str(input('Informe seu sexo: [M/F] ')).strip().upper()[0]
while sexo not in 'MmFf':
    sexo = str(input('Sexo inválido. Tente novamente: ')).strip().upper()[0]
print('Sexo {} resgistrado com sucesso.'.format(sexo))   