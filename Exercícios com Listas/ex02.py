lista = list()
for n in range(10):
    lista.append(float(input('Informe um número real: ')))
    
print()
lista.sort(reverse = True)
print(lista)