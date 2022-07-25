from random import randint
numeros = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))
print('Os números sorteados foram: ', end = '')
for n in numeros:
    print(f'{n} ', end = '')
print('')
print('-' * 30)
print(f'O maior valor mostrado foi o {max(numeros)}')
print('-' * 30)
print(f'O menor valor mostrado foi o {min(numeros)}')