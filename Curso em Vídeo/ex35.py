a=float(input('Primeiro segmento: '))
b=float(input('Segundo segmento: '))
c=float(input('Terceiro segmento: '))
if a < b+c and b < c+a and c < a+b:
    print('O triângulo \033[1;32mPODE\033[m ser formado pelos segmentos acima.')
else:
    print('O triângulo \033[1;31mNÃO PODE\033[m ser formado pelos segmentos acima.')