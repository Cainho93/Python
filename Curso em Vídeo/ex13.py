def main():
    salario=float(input('Qual o seu salário ?: R$ '))
    aumento=salario+(salario*15/100)
    print('Com o aumento salarial de 15% o seu salário passou de R$ {} para R$ {}'.format(salario,aumento))
main()