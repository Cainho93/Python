def main():
    n=float(input('Digite o preço do produto: R$ '))
    d=n-(n*5/100)
    print('O produto custa R$ {} mas com 5% desconto fica R$ {}.'.format(n,d))
main() 