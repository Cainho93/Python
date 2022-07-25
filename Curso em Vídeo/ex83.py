expr = str(input('Digite a expressão: '))
lista = []
for simbolo in expr:
    if simbolo == '(':
        lista.append('(')
    elif simbolo == ')':
        if len(lista) > 0:
            lista.pop()
        else:
            lista.append(')')
if len(lista) == 0:
    print('A expressão é válida')
else:
    print('A expressão é inválida')