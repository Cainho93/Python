salario=float(input('Qual o salário do funcionário?: R$ '))
if salario <= 1250:
    aumento = salario + (salario*15/100) # Aumento em 15% 
else:
    aumento = salario + (salario*10/100) # Aumento em 10%
print('Quem ganhava R$ {:.2f} agora ganha R$ {:.2f}'.format(salario,aumento))