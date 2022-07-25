n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
while n2 < n1:
    print('\033[1mO 1º valor tem que ser menor que o 2º valor\033[m')
    n1 = int(input('Digite um número: '))
    n2 = int(input('Digite outro número: '))
else:
    s = 0
    for n in range(n1 + 1, n2):
        print(n, end = ' ')
        s += n
    print(f'\nA soma é igual a {s}')