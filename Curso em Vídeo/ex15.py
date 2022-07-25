def main():
    km=float(input('Quantos Km o carro andou?: '))
    dias=int(input('Quantos dias o carro foi alugado?: '))
    preco_km=km*0.15
    preco_dias=dias*60
    total_pagar=preco_km+preco_dias
    print('O total a pagar pelo carro é R$ {:.2f}'.format(total_pagar))
main()