print('Gerador da PA')
print('-=' * 10)
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
termo = primeiro
cont = 1
mais = 10
total = 0
while mais != 0:
    total += mais
    while cont <= total:
        print('{} -> '.format(termo), end = '')
        termo += razao
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos termos a mais?: '))
print('A PA foi finalizada com {} termos'.format(total))