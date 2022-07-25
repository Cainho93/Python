pmaior = 0
pmenor = 0
for pess in range(1, 6):
    peso = float(input('Digite o {}º peso: '.format(pess)))
    if pess == 1:
        pmaior = peso
        pmenor = peso
    else:
        if peso > pmaior:
            pmaior = peso
        if peso < pmenor:
            pmenor = peso
print('O maior peso é {}Kg'.format(pmaior))
print('O menor peso é {}Kg'.format(pmenor))