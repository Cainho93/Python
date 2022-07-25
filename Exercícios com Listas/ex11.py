vetorA = list()
vetorB = list()
vetorC = list()
vetorD = list()

print('VetorA')
for n in range(10):
    vetorA.append(int(input('Informe um valor para a 1ª lista: ')))
print('-' * 40)
print('VetorB')    
for n in range(10):
    vetorB.append(int(input('Informe um valor para a 2ª lista: ')))
print('-' * 40)
print('VetorC')
for n in range(10):
    vetorC.append(int(input('Informe um valor para a 3ª lista: ')))

for n in range(10):
    vetorD.append(vetorA[n])
    vetorD.append(vetorB[n])
    vetorD.append(vetorC[n])
    
print(F'''
VetorA = {vetorA}
VetorB = {vetorB}
VetorC = {vetorC}
VetorD = {vetorD}''')