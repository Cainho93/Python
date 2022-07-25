num = list()

while True:
    n = float(input('Informe uma nota (-1 para parar): '))
    if n != -1:
        num.append(n)
    else:
        break

print('-' * 40)

print(f'No total foram {len(num)} números lidos')

print('Notas lidas na ordem correta:')
for n in range(len(num)):
    print(f'[{num[n]}] ', end = '')
    
print('\nNotas lidas na ordem inversa:')
for n in range(len(num)):
    print(f' -{num[::-1][n]}')
    
print(f'A soma entre as notas é {sum(num):.2f}')

media = sum(num) / len(num)
print(f'A média das notas é {media:.2f}')

print('Notas acima da média:')
for n in range(len(num)):
    if num[n] > media:
        print(f'[{num[n]}] ', end = '')
        
print('\nNotas abaixo de 7.0:')
for n in range(len(num)):
    if num[n] < 7:
        print(f'[{num[n]}] ', end = '')
        
print('\n\033[1;34mFIM DE PROGRAMA\033[m')