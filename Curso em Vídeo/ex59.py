from time import sleep
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
opcao = 0
while opcao != 5:
    print('')
    print('''OPÇÕES
======================
[ 1 ] Somar
[ 2 ] Multiplicar
[ 3 ] Maior 
[ 4 ] Novos números
[ 5 ] Sair do programa
======================''')
    opcao = int(input('Digite sua opção: '))
    if opcao == 1:
        soma = n1 + n2
        print('A soma entre {} + {} = {}'.format(n1, n2, soma))
    elif opcao == 2:
        multiplicacao = n1 * n2
        print('A multiplicação entre {} x {} = {}'.format(n1, n2, multiplicacao))
    elif opcao == 3:
        if n1 > n2:
            maior = n1
            print('Entre {} e {} o maior é o {}'.format(n1, n2, maior))
        elif n1 < n2:
            maior = n2
            print('Entre {} e {} o maior é o {}'.format(n1, n2, maior))
    elif opcao == 4:
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    elif opcao == 5:
        print('Finalizando', end = '')
        sleep(0.6)
        print('.', end = '')
        sleep(0.6)
        print('.', end = '')
        sleep(0.6)
        print('.')
        sleep(1)
    else:
        print('Opção Inválida!')
print('Fim do programa.')