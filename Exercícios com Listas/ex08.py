idades = list()
alturas = list()

for pess in range(5):
    print(f'{pess + 1}ª pessoa\n')
    idade = int(input('Idade: '))
    altura = float(input('Altura: '))
    print()
    idades.append(idade)
    alturas.append(altura)
    
print(f'''Ordem inversa:
Idades: {idades[::-1]}
Alturas: {alturas[::-1]}''')