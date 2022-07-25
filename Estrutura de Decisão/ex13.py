n1 = float(input('Informe a 1ª nota: '))
n2 = float(input('Informe a 2ª nota: '))
med = (n1 + n2) / 2
conceito = ''
sit = ''
if med >= 9 and med <= 10:
    conceito = 'A'
    sit = 'APROVADO'
elif med >= 7.5 and med < 9:
    conceito = 'B'
    sit = 'APROVADO'
elif med >= 6 and med < 7.5:
    conceito = 'C'
    sit = 'APROVADO'
elif med >= 4 and med < 6:
    conceito = 'D'
    sit = 'REPROVADO'
else:
    conceito = 'E'
    sit = 'REPROVADO'
print('-' * 25)
print(f'''Notas: {n1:.2f} / {n2:.2f}
Média: {med}
Conceito: {conceito}
Situação: {sit}''')