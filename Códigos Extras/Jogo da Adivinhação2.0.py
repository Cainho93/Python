from random import randint
a = ('~' * 21)
tentativas = 5
adm = True
computador = randint(0, 30)
print('{:=^41}'.format('\033[1;36m Jogo da Adivinhação \033[m'))
print('')
print('Você terá 5 chances para acertar o meu número')
print('')
while adm == True:
    print(a)
    usuario = int(input('Dê seu palpite: '))
    if usuario > computador:
        tentativas -= 1
        print('\033[1;33mMENOS...\033[m')
        print('Você tem {} tentativas'.format(tentativas))
    if usuario < computador:
        tentativas -= 1
        print('\033[1;35mMAIS...\033[m')
        print('Você tem {} tentativas'.format(tentativas))
    if usuario == computador:
        print('\033[1;32mACERTOU!!!\033[m')
        adm = False
    if tentativas == 0:
        print('Acabaram suas chances de acertar meu número')
        adm = False
print(a)