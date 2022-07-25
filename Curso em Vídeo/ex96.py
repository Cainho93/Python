def area(larg, alt):
    a = larg * alt
    print(f'A área do terreno {larg} x {alt} é de {a}m².')
    
print('''Controle de Terrenos
--------------------''') 
l = float(input('Largura (m): '))
a = float(input('Altura (m): '))

area(l, a)    