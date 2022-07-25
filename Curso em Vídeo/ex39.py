from datetime import date
atual=date.today().year
ano=int(input('Ano de nascimento: '))
sexo=str(input('Qual seu sexo?: ')).upper()
idade= atual - ano
print('Quem nasceu em {} tem {} anos em {}'.format(ano,idade,atual))
if sexo == 'FEMININO':
    print('Você não precisa se alistar obrigatoriamente.')
if idade == 18 and sexo == 'MASCULINO':
    print('Você tem que se alistar IMEDIATAMENTE!')
elif idade < 18 and sexo == 'MASCULINO':
    saldo = 18 - idade
    print('Ainda faltam {} anos para o alistamento.'.format(saldo))
    ano_alist= atual + saldo
    print('Seu alistamento será em {}'.format(ano_alist))
elif idade > 18 and sexo == 'MASCULINO':
    saldo = idade - 18
    print('Ja se passaram {} anos, você NÃO pode se alistar.'.format(saldo))
    ano_alist= atual - saldo
    print('Seu alistamento foi em {}'.format(ano_alist))