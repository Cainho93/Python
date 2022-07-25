from time import sleep
from math import sqrt
a = float(input('Informe o valor de A: '))
delta = raiz = raiz1 = raiz2 = 0
if a == 0:
    print('Não é possível realizar a conta (NÃO É EQUAÇÃO DE 2º GRAU)')    

else:
    b = float(input('Informe o valor de B: '))
    c = float(input('Informe o valor de C: '))
    print('-' * 30)
    print('Calculando Delta', end = '')
    sleep(0.6)
    print('.', end = '')
    sleep(0.8)
    print('.', end = '')
    sleep(0.8)
    print('.')
    sleep(0.8)
    delta = b*b - (4*a*c)
    print(delta)
    if delta < 0:
        print('Não é possível calcular raízes de delta negativo')
    elif delta == 0:
        print('O delta igul a 0 possue uma raiz')
        raiz = -b / (2*a)
    else:
        raiz1 = (-b + math.sqrt(delta) ) / (2*a)
        raiz2 = (-b - math.sqrt(delta) ) / (2*a)
        print(f'As raizes são: [{raiz1:.2f}, {raiz2:.2f}] ')