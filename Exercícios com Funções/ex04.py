def ex_6(h, m):
    if 0 < h <= 12 and 0 < m < 60:
        print(f'{h}:{m} a.m')
    elif 12 < h < 24 and 0 < m < 60:
        print(f'{h - 12}:{m} p.m')
    else:
        print('Valor inválido')

while True:
    hora = int(input('Hora: '))
    if hora > 24:
        break
    minuto = int(input('Minuto: '))
    ex_6(hora, minuto)
    print('=' * 12)