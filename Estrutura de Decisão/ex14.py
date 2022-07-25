l1 = float(input('Informe o 1º lado: '))
l2 = float(input('Informe o 2º lado: '))
l3 = float(input('Informe o 3º lado: '))

if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l1 + l2:
    print('Os 3 segmentos \033[1;32mPODEM\033[m formar um triângulo ', end = '')
    if l1 == l2 == l3:
        print('\033[1;34mEQUILÁTERO\033[m')
    elif l1 != l2 != l3 != l1:
        print('\033[1;35mESCALENO\033[m')
    else:
        print('\033[1;36mISÓSCELES\033[m')
else:
    print('Os 3 segmentos \033[1;31mNÃO PODEM\033[m formar um triângulo')