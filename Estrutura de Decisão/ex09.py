a = int(input('Informe o 1º valor: '))
b = int(input('Informe o 2º valor: '))
c = int(input('Informe o 3º valor: '))

if a >= b and a >= c and b >= c:
    print(f'A ordem decrescente será {a} -> {b} -> {c}')
elif a >= b and a >= c and c >= b:
    print(f'A ordem decrescente será {a} -> {c} -> {b}')
elif b >= a and b >= c and a >= c:
    print(f'A ordem decrescente será {b} -> {a} -> {c}')
elif b >= a and b >= c and c >= a:
    print(f'A ordem decrescente será {b} -> {c} -> {a}')
elif c >= a and c >= b and a >= b:
    print(f'A ordem decrescente será {c} -> {a} -> {b}')
elif c >= a and c >= b and b >= a: 
    print(f'A ordem decrescente será {c} -> {b} -> {a}')
