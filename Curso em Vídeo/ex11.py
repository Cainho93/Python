def main():
    largura=float(input('Digite a largura: '))
    altura=float(input('Digite a altura: '))
    area=largura*altura
    print('Com a multiplicação da largura {} e da altura {} temos a área de {}m²'.format(largura,altura,area))
    tinta=area/2
    print('A quantidade necessária de tinta para pintar uma área de {}m² é {}L'.format(area,tinta))
main()