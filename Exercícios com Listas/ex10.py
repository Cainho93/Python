lista1 = list()
lista2 = list()
lista3 = list()

for n in range(10):
    lista1.append(int(input('Informe um valor para a 1ª lista: ')))
print('-' * 40)    
for n in range(10):
    lista2.append(int(input('Informe um valor para a 2ª lista: ')))
    
for n in range(10):
    lista3.append(lista1[n])
    lista3.append(lista2[n])
    
print(f'''
Lista1 = {lista1}
Lista2 = {lista2}
Lista3 = {lista3}''')