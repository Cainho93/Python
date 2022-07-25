while True:
    print()
    atleta = str(input('Nome do atleta: '))
    if atleta == '':
        break
    else:
        lista_saltos = list()
        print('~' * 14)
        for salto in range(5):
            saltos = float(input(f'{salto + 1}º salto: '))
            lista_saltos.append(saltos)
        print('~' * 14) 
        num_ext = ['Primeiro', 'Segundo', 'Terceiro', 'Quarto', 'Quinto']
        print('\033[1mResultado Final:\033[m')
        print(f' Atleta: {atleta.capitalize()}')
        print('\033[1m SALTOS:\033[m')
        for n in range(len(lista_saltos)):
            print(f'  -{num_ext[n]} salto: {lista_saltos[n]}m')
        print(f' \033[1mMelhor salto:\033[m {max(lista_saltos)}m')
        print(f' \033[1mPior salto:\033[m {min(lista_saltos)}m')
        print(f' \033[1mMédia dos saltos\033[m {sum(lista_saltos) / len(lista_saltos)}m')