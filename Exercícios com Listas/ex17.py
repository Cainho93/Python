salarios = list()
abonos = list()
while True:
    salario = float(input('Salário [0 INTERROMPE]: R$ '))
    if salario <= 0:
        break
    else:
        salarios.append(salario)
    tot_abono = min_abono = 0
    for salario in salarios:
        abono = salario * 0.2
        if abono <= 100:
            abono = 100.0
            min_abono += 1
        tot_abono += abono
    abonos.append(abono)
    
print('-' * 40)

for salario, abono in zip(salarios, abonos):
    print(f'R$ {salario:.2f} - R$ {abono:.2f}')
print(f'Foram processados {len(salarios)} colaboradores')  
print(f'Total gasto com abonos: R$ {tot_abono:.2f}')  
print(f'Valor minimo pago à {min_abono} colaboradores')
print(f'Maior valor de abono pago: R$ {max(abonos)}')