nome = str(input('Nome: ')).strip().capitalize()
while len(nome) < 3:
    nome = str(input('Informe um nome com pelo menos 3 letras: ')).strip().capitalize()
idade = int(input('Idade: '))
while 0 > idade or idade > 150:
    idade = int(input('Informe uma idade entre 0 e 150 anos: '))
salario = float(input('Salário: R$ '))
while salario <= 0:
    salario = float(input('Informe um salário acima de R$ 0,00: R$ '))
sexo = str(input('Sexo [M/F]: ')).upper()[0]
while sexo not in 'MF':
    sexo = str(input('Informe um sexo dentre [M/F]: ')).upper()[0]
estado_civil = str(input('Estado Civil [S/C/V/D]: ')).upper()[0]
while estado_civil not in 'SCVD':
    estado_civil = str(input('Informe o Estado Civil dentre [S/C/V/D]: ')).upper()[0]