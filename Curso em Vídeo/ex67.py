num = 0
while True:
    print('=' * 40)
    num = int(input('Digite um número para ver sua tabuada: '))
    print('=' * 40)
    if num <= 0:
        break
    for c in range(1, 11):
        print(f'{num} x {c} = {num * c}')
print('PROGRAMA TABUADA ENCERRADO. Volte sempre!')