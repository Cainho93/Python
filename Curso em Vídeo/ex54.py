somaidade = 0
mediaidade = 0
maioridadehomemvelho = 0
homemvelho = ''
totmulher = 0 
for p in range (1, 5):
    print('==== {}ª PESSOA ===='.format(p))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    somaidade += idade
    if p == 1 and sexo in 'Mm':
        homemvelho = nome
        maioridadehomemvelho = idade
    if sexo in 'Mm' and idade > maioridadehomemvelho:
        homemvelho = nome
        maioridadehomemvelho = idade
    if sexo in 'Ff' and idade < 20:
        totmulher += 1
mediaidade = somaidade / 4
print('A média de idade do grupo é de {:.1f} anos'.format(mediaidade))
print('O homem mais velho se chama {} e tem {} anos'.format(homemvelho, maioridadehomemvelho))
print('Ao todo são {} mulheres menores de 20 anos'.format(totmulher))