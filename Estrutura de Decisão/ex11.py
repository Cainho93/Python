#Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
#salários até R$ 280,00 (incluindo) : aumento de 20%
#salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
#salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
#salários de R$ 1500,00 em diante : aumento de 5% 
#Após o aumento ser realizado, informe na tela:
#o salário antes do reajuste;
#o percentual de aumento aplicado;
#o valor do aumento;
#o novo salário, após o aumento.
salario_inicial = float(input('Quanto você ganha atualmente: R$ '))
salario_final = 0

if salario_inicial <= 280:
    salario_final = salario_inicial + (salario_inicial * 20 / 100)
    percentual = '20%'
if salario_inicial > 280 and salario_inicial <= 700:
    salario_final = salario_inicial + (salario_inicial * 15 / 100)
    percentual = '15%'
if salario_inicial > 700 and salario_inicial <= 1500:
    salario_final = salario_inicial + (salario_inicial * 10 / 100)
    percentual = '10%'
if salario_inicial > 1500:
    salario_final = salario_inicial + (salario_inicial * 5 / 100)
    percentual = '5%'

print('-' * 40)
print(f'Salário antes reajuste: R$ {salario_inicial:.2f}')
print(f'Com {percentual} de aumento')
valor_reajuste = salario_final - salario_inicial
print(f'O valor de aumento é de R$ {valor_reajuste:.2f}')
print(f'O valor após reajuste: R$ {salario_final:.2f}')