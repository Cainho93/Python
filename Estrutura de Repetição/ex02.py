nome = input('Informe o nome de usuário: ').strip()
senha = input('Informe sua senha: ')
while True:
    if senha == nome:
        print()
        print('\033[1mA senha não pode ser igual ao nome.\033[m')
        senha = input('Informe sua senha: ')
    else:
        print('\033[1;32mCadastro Realizado\033[m')
        break