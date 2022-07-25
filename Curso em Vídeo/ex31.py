km=float(input('Quantos km você percorreu?: '))
if km<=200:
    preco=km*0.50
else:
    preco=km*0.45
print('Você terá que pagar R${:.2f}'.format(preco))