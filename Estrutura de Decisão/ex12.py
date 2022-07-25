dia = int(input('Digite um número de 1 à 7: '))

print('-' * 30)
if dia == 1:
    print('Hoje é Domingo')
elif dia == 2:
    print('Hoje é Segunda-feira')
elif dia == 3:
    print('Hoje é Terça-feira')
elif dia == 4:
    print('Hoje é Quarta-feira')
elif dia == 5:
    print('Hoje é Quinta-feira')
elif dia == 6:
    print('Hoje é Sexta-feira')
elif dia == 7:
    print('Hoje é Sábado')
else:
    print('Valor inválido')