str1 = str(input(''))
str2 = str(input(''))
print(f'Tamanho de "{str1}": {len(str1)} caracteres')
print(f'Tamanho de "{str2}": {len(str2)} caracteres')
if len(str1) == len(str2):
    print('O tamanho das duas strings são iguais')
else:
    print('O tamanho das duas strings são diferentes')
if str1 == str2:
    print('As duas strings possuem o mesmo conteúdo')
else:
    print('As duas strings não possuem o mesmo conteúdo')