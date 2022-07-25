num = int(input('Informe um número menor que 1000: '))

if num >= 1000:
    print('Valor INVÁLIDO')        
# Extraindo a unidade, dezena e centena
unidade = num % 10
num = (num - unidade) / 10
dezena = num % 10
num = (num - dezena) / 10
centena = num % 10

# Deixando a centena e a dezena inteiros
centena = int(centena)
dezena = int(dezena)

print(f'{centena} centena(s), {dezena} dezena(s) e {unidade} unidade(s)')