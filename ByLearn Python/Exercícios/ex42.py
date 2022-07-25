# Conversor de Moedas
real=float(input('Valor em R$: '))
dolar=real/5.46
euro=real/6.63
print('Na conversão do real pro dólar temos U${:.2f}'.format(dolar))
print('Na conversão do real pro euro temos €{:.2f}'.format(euro))