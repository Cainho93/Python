listanum = []
while True:
    listanum.append(int(input('Digite um valor: ')))
    resp = str(input('Quer continuar [S/N] ')).strip().upper()[0]
    while resp not in 'SN':
        resp = str(input('Quer continuar [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print('-=' * 26)
print(f'Foram digitados {len(listanum)} números')
listanum.sort(reverse = True)
print(f'Lista em ordem decrescente: {listanum}')
if 5 in listanum:
    print('O número 5 foi encontrado na lista')
else:
    print('O número 5 não foi encontrado na lista')