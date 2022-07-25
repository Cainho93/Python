# SIMULADOR DE LOJA SIMPLES
print('{:=^40}'.format('LOJAS FACCIONI'))
preco=float(input('Qual o valor do produto?: R$ '))
print('''FORMAS DE PAGAMENTO
[ 1 ] à vista no dinheiro/cheque
[ 2 ] à vista no cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
opcao=int(input('Sua opção: '))
if opcao == 1:
    pagar= preco-(preco*10/100)
elif opcao == 2:
    pagar= preco-(preco*5/100) 
elif opcao == 3:
    pagar= preco
    parcela= preco / 2
    print('Parcelado em 2x o valor é de R$ {:.2f}'.format(parcela))
elif opcao == 4:
    parcelado=int(input('Em quantas parcelas: '))
    pagar= preco+(preco*20/100)
    parcela= pagar / parcelado
    print('Parcelado em {}x o valor é de R$ {:.2f} COM JUROS'.format(parcelado,parcela))
else:
    print('Opção \033[0;31mINVÁLIDA!\033[m Tente novamente')
print('Sua compra de R$ {:.2f} vai custar R$ {:.2f} no final'.format(preco,pagar))