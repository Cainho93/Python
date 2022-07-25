from datetime import date
from time import sleep
nasc=int(input('Ano de nascimento: '))
ano_atual=date.today().year
idade = ano_atual - nasc
print('O atleta tem {} anos'.format(idade))
print('PROCESSANDO CATEGORIA...')
sleep(2)
if idade <= 9:
    print('MIRIM')
elif idade <= 14:
    print('INFANTIL')
elif idade <= 19:
    print('JUNIOR')
elif idade <= 25:
    print('SÊNIOR')
else:
    print('MASTER')