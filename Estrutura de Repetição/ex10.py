num = int(input('Digite um número para ver sua tabuada: '))
print('=' * 14)
for n in range(1, 11):
    print(f'  {num} x {n} = {num * n}')
print('=' * 14)