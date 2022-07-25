kg=float(input('Qual seu peso?: '))
alt=float(input('Qual a sua altura?: '))
# Calcular o IMC
imc= kg/(alt**2)
print('Seu IMC é {:.1f}'.format(imc))
if imc < 18.5:
    print('Você está ABAIXO DO PESO')
elif imc >= 18.5 and imc < 25:
    print('Você está no PESO IDEAL')
elif imc >= 25 and imc < 30:
    print('Você está com SOBREPESO')
elif imc >= 30 and imc < 40:
    print('Você está com OBESIDADE')
elif imc >= 40:
    print('CUIDADO! Você está com OBESIDADE MÓRBIDA')