frase = str(input('Frase: ')).strip().upper()
palavra = frase.split()
junto = ''.join(palavra)
inverso = ''
for letra in range(len(junto) -1, -1, -1):
    inverso += junto[letra]
print(f'O inverso de {junto} é {inverso} e ela;')
if inverso == junto:
    print('É um palíndromo!')
else:
    print('Não é um palíndromo!')