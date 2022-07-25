km=int(input('Qual a velocidade atual do carro?: '))
if km > 80:
    print('MULTADO! Você excedeu o limite de velocidade que é 80Km/h')
    multa=(km-80)*7
    print('O valor que você terá que pagar é de R${}'.format(multa))
else:
    print('Tenha um bom dia! Dirija com segurança!')