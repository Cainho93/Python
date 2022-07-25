lista = list()
soma = 0
for n in range(5):
    lista.append(int(input('Informe um valor: ')))
    soma += (lista[len(lista) - 1] ** 2)
    
print(f'A soma dos quadrados dos números é igual a {soma}')