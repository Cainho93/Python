def main():
    from math import sqrt 
    co=float(input('Cateto oposto: '))
    ca=float(input('Cateto adjacente: '))
    h=(co**2 + ca**2)
    print('A hipotenusa é {:.2f}'.format(sqrt(h)))
main()