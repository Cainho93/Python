num = cont = soma = 0
num = int(input('Digite um valor: [999 para parar] '))
while num != 999:
    soma += num
    cont += 1
    num = int(input('Digite um valor: [999 para parar] '))
print('Foram digitados {} números e a soma entre eles foi {}'.format(cont, soma))