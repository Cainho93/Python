idades = list()
alturas = list()
for pess in range(30):
    print(f'{pess + 1}ª Pessoa:')
    idade = int(input('Idade: '))
    altura = float(input('Altura: '))
    idades.append(idade)
    alturas.append(altura)
    
media_altura = sum(alturas) / len(alturas)
cont = 0
for p in range(0, len(idades)):
    if idades[p] >= 13 and alturas[p] < media_altura:
        cont += 1
print(f'A média de altura é de {media_altura:.2f}')    
print(f'{cont} pessoas com idade igual ou superior a 13 anos que tem altura inferior a média de altura do grupo')