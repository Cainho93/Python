string = str(input('Frase: ')).lower()

print(f"a: Quantos espaços em branco existem na frase?: {string.count(' ')}")
print(f"""b: Quantas vezes aparecem as vogais a, e, i, o, u?:
Aa: {string.count('a')} vezes
Ee: {string.count('e')} vezes
Ii: {string.count('i')} vezes
Oo: {string.count('o')} vezes
Uu: {string.count('u')} vezes""")