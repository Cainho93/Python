#Para atender a todos os clientes, cada cliente poderá levar apenas um dos tipos de carne da promoção, 
#porém não há limites para a quantidade de carne por cliente. Se compra for feita no cartão Tabajara o cliente receberá 
#ainda um desconto de 5% sobre o total da compra. Escreva um programa que peça o tipo e a quantidade de carne comprada 
#pelo usuário e gere um cupom fiscal, contendo as informações da compra: 
#tipo e quantidade de carne, preço total, tipo de pagamento, valor do desconto e valor a pagar.
tipo_carne = int(input('Qual o tipo de carne desejada? [Filé Duplo - 1/ Alcatra - 2/ Picanha - 3]: '))
kg_carne = int(input('Quantos Kgs de carne?: '))
resposta = str(input('Vai pagar com o cartão Tabajara? [S/N]: ')).strip().upper()[0]

if tipo_carne == 1:
    nome = 'Filé Duplo'
    if kg_carne <= 5:
        preco = kg_carne * 4.90
    else:
        preco = kg_carne * 5.80

if tipo_carne == 2:
    nome = 'Alcatra'
    if kg_carne <= 5:
        preco = kg_carne * 5.90
    else:
        preco = kg_carne * 6.80
    
if tipo_carne == 3:
    nome = 'Picanha'
    if kg_carne <= 5:
        preco = kg_carne * 6.90
    else:
        preco = kg_carne * 7.80
        
if resposta == 'S':
    r = 'Cartão Tabajara'
    total = preco - (preco * 5 / 100)
else:
    r = 'Dinheiro'
    total = preco
    
print(f'''
===============CUPOM FISCAL===============

Tipo da carne......................... {nome}
Quantidade da carne................... {kg_carne}Kg
Preço bruto........................... R${preco:.2f}
Forma de pagamento.................... {r}
Total com desconto.................... R${total:.2f}''')