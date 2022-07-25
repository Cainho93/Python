# Criar um programa de DECIDA POR MIM 
# 10 à 20 respostas prontas
# Oq pode-se utilizar: Laços, listas, random(choice), condicionais
# Perguntas: Para onde eu irei hoje, Oque eu como hoje, Vamos jogar futebol?, Com qual roupa eu saio hoje
from random import choice
from time import sleep
print('{:=^40}'.format('\033[1mDECIDA POR MIM\033[m'))
print('-=' * 28)
print('Computador... Hoje eu irei deixar você decidir meu dia')
print('Cada número será uma pergunta diferente')
print('-=' * 28)
opcao = 0
a = ('~' * 42)
while opcao != 5:
    print('')
    print('''Perguntas
    [ 1 ] Para onde eu vou hoje?
    [ 2 ] O que eu vou comer?
    [ 3 ] Qual jogo eu vou jogar?
    [ 4 ] Com qual roupa eu saio hoje?
    [ 5 ] Sair do programa
    ''')
    opcao = int(input('Escolha qualquer um: '))
    print('')
    if opcao == 1:
        print(a)
        print('Eae computador pra onde eu vou? ')
        print('')
        resp = ['Fica em casa hoje', 'Vai pro shopping com os mlk', 
                'Vai jogar um fut', 'Vai andar de skate', 
                'Vai la no Point tomar um açaí']
        resp_comp = choice(resp)
        print('Computador: {}'.format(resp_comp))
        print(a)
    if opcao == 2:
        print(a)
        print('Me diga oque eu vou comer hoje?')
        print('')
        resp = ['Come a comida da vó', 'Come um lanche do McDonalds', 
               'Come um yakissoba hoje', 'Fica de jejum kkkk',
               'Pede um marmitex']
        resp_comp = choice(resp)
        print('Computador: {}'.format(resp_comp))
        print(a)
    if opcao == 3:
        print(a)
        print('Oque eu jogo hoje?')
        print('')
        resp = ['Joga um fortnite cara', 'Vai de Rocket League hoje', 
                'Joga Fifa, faz tempo que você não joga',
                'Se os mlk estiverem no Paladins entra lá', 
                'Desenterra o Minecraft e vai de lobo solitário']
        resp_comp = choice(resp)
        print('Computador: {}'.format(resp_comp))
        print(a)
    if opcao == 4:
        print(a)
        print('Escolha as minhas roupas de sair hoje')
        print('')
        resp = ['Camiseta do Corinthians, shorts da Nike e chinelo Nike', 
                'Camiseta Why Not?, calça preta da Nike e Vans',
                'Camiseta da Lacoste preta, shorts rasgado, chinelo Nike', 
                'Moletom da Jordan, calça da Oakley e Yeezy',
                'Camiseta da Lacoste branca, calça azul escura da nike e Nike Air Max']
        resp_comp = choice(resp)
        print('Computador: {}'.format(resp_comp))
        print(a)
    if opcao == 5:
        print(a)
        print('Finalizando programa', end = '')
        sleep(0.6)
        print('.', end = '')
        sleep(0.6)
        print('.', end = '')
        sleep(0.6)
        print('.')
        sleep(1)
        print(a)
        print('Operação finalizada com sucesso')