caract = list()
conso = 0
for n in range(10):
    caract.append(str(input('Informe uma letra: ')))
    char = caract[n]
    if char not in 'aeiou':
        conso += 1
        
print(f'São um total de {conso} consoantes')