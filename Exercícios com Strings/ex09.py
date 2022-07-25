cpf = input('CPF (xxx.xxx.xxx-xx): ')

if cpf[3] != '.' or cpf[7] != '.' or cpf[11] != '-':
    print('O formato de CPF está incorreto!')
else:
    print('CPF aprovado com sucesso!')