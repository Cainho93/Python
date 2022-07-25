num=int(input('Digite um número inteiro: '))
print('''Escolha uma das bases para conversão:
[ 1 ] Converter para BINÁRIO.
[ 2 ] Converter para OCTAL.
[ 3 ] Converter para HEXADECIMAL.''')
opcao=int(input('Sua opção: '))
if opcao == 1:
    print('{} convertido para BINÁRIO é igual a {}'.format(num,bin(num)[2:])) # bin converte para BINÁRIO
elif opcao == 2:
    print('{} convertido para OCTAL é igual a {}'.format(num,oct(num)[2:])) # oct converte para OCTAL
elif opcao == 3:
    print('{} convertido para HEXADECIMAL é igual a {}'.format(num,hex(num)[2:])) # hex converte para HEXADECIMAL
else:
    print('Opcão \033[4;31mÍNVALIDA!')