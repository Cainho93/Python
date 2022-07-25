n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
m = (n1+n2)/2
print('Com as notas {} e {} temos a média {}'.format(n1,n2,m))
if m < 5:
    print('\033[4;31mREPROVADO!')
elif m < 7 and m > 5:
    print('\033[4;33mRECUPERAÇÃO!')
elif m >= 7:
    print('\033[4;32mAPROVADO!')