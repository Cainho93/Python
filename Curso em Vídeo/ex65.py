num = media = maior = menor = quant = soma = 0
resp = 'S'
while resp in 'S':
    num = float(input('Digite um valor: '))
    resp = str(input('Quer continuar: [S/N] ')).strip().upper()[0]
    soma += num
    quant += 1
    if quant == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
media = soma / quant
print('Foram digitados {} números e a média entre eles foi {:.2f}'.format(quant, media))
print('O maior valor lido foi o {} e o menor valor lido foi o {}'.format(maior, menor))