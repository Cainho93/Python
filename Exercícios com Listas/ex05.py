num = list()
par = list()
impar = list()
for n in range(20):
    num.append(int(input(f'Informe o {n + 1}º valor: ')))
    
for i, v in enumerate(num):
    if v % 2 == 0:
        par.append(v)
    else:
        impar.append(v)
        
print(f'''
Números: {num}
Pares: {par}
Ímpares: {impar}''')