from datetime import date
ano_atual = date.today().year
registro = dict()
registro['nome'] = str(input('Nome: '))
nasc = (int(input('Ano de nascimento: ')))
registro['idade'] = ano_atual - nasc
registro['ctps'] = int(input('Carteira de trabalho [0 se não tiver]: '))
if registro['ctps'] != 0:
    registro['ano de contratação'] = int(input('Ano de contratação: '))
    registro['salário'] = int(input('Salário: '))
    registro['aposentadoria'] = registro['idade'] + ((registro['ano de contratação'] + 35) - ano_atual)
print('-=' * 30)
for k, v in registro.items():
    print(f'- {k.capitalize()} tem o valor de {v}')