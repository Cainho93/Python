while True:
    num = int(input('Digite um número entre 0 e 10: '))
    if num >= 0 or num <= 10:
        break
    else:
        print('\033[31mNúmero INVÁLIDO.\033[m Números entre 0 e 10')