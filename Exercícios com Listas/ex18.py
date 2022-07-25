carros = list()
km_litros = list()

for car in range(5):
    carros.append(str(input(f'{car + 1}º Carro: ')))
    km_litros.append(float(input('Km por litro: ')))
    

menor = cont = 0
carro = ''
print('-' * 40)
for car in carros:
    custo = 1000 / km_litros[cont]
    gasto = custo * 2.25
    print(f'{car.capitalize()}  -  {km_litros[cont]}l  -  {custo:.2f}l  -  R${gasto:.2f}')
    if cont == 0:
        menor = custo
        carro = car
    elif menor > custo:
        menor = custo
        carro = car
    cont += 1
        
print(f'O carro mais econômico é {carro.capitalize()}')    