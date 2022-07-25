bas = int(input('Informe a base: '))
exp = int(input('Informe o expoente: '))
pot = 1
for c in range(exp):
    pot *= bas
    c += 1
print(f'{bas} elevado a {exp} é igual a {pot}')