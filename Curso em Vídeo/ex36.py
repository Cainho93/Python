casa=float(input('Qual o valor da casa?: R$ '))
salario=float(input('Qual o seu salário?: R$ '))
anos=int(input('Em quantos anos você pretende pagar a casa?: '))
prestacao= casa / (anos*12)
minimo= salario * 30 / 100
print('Para comprar uma casa de R$ {:.2f} em {} anos a prestação será de R$ {:.2f}'.format(casa,anos,prestacao))
if prestacao <= minimo:
    print('Empréstimo \033[0;32mACEITO')
else:
    print('Empréstimo \033[0;31mNEGADO')