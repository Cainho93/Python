nome = str(input('Informe seu nome: ')).strip()
n1 = float(input('Informe sua 1ª nota: '))
n2 = float(input('Informe sua 2ª nota: '))
m = (n1 + n2) / 2
print(f'{nome.capitalize()} foi:')
if m >= 7:
    print(f'APROVADO com {m}')
if m < 7:
    print(f'REPROVADO com {m}')