def main():
    n=int(input('Digite um valor: '))
    d=n*2
    t=n*3
    r=n**(1/2)
    print('O número é {}.\nSeu dobro é {}.\nSeu triplo é {}.\nSua raiz quadrada é {:.2f}.'.format(n,d,t,r))
main()