s = 0
for n in range(5):
    num = float(input(f'Informe o {n + 1}º número: '))
    s += num
m = s / 5
print(f'A soma de todos os números é igual a {s}\nA média é igual a {m}')