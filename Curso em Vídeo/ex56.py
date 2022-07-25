totidade = 0
mediaidade = 0
homemvelho = ''
maioridadehomemvelho = 0
totmulher = 0
for p in range(1, 5):
    print('==== {}ª PESSOA ===='.format(p))
    nome = str(input('Nome: ')).capitalize()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo: '))
    totidade += idade
    mediaidade = totidade / 4
    if p == 1 and sexo in 'Mm':
        maioridadehomemvelho = idade
        homemvelho = nome
    if sexo in 'Mm' and idade > maioridadehomemvelho:
        maioridadehomemvelho = idade
        homemvelho = nome
    if sexo in 'Ff' and idade < 20:
        totmulher += 1
print('A média de idade do grupo é {}'.format(mediaidade))
print('O homem mais velho é o {} com {} anos'.format(homemvelho, maioridadehomemvelho))
print('No grupo temos {} mulheres com menos de 20 anos'.format(totmulher))