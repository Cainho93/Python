notas = list()
for n in range(4):
    notas.append(float(input(f'Informe a {n + 1}ª nota: ')))
    
media = sum(notas) / len(notas)

print(f'''
Notas: {notas}
Média: {media:.2f}''')