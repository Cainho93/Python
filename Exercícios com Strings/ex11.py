from random import choice

palavras = ['abacate', 'abacaxi', 'goiaba', 'kiwi', 'laranja', 'tangerina', 'cereja', 'abelha', 'anaconda', 'baleia',
'borboleta', 'cachorro', 'coelho', 'golfinho', 'pinguim', 'andorra', 'alemanha', 'brasil', 'china', 'espanha', 'italia', 
'venezuela']
palavra = choice(palavras)
chances = 6
tentativas = []
alfabeto = list('abcdefghijklmnopqrstuvwxyz')

while True:
    print(tentativas)
    print(f'Chances: {chances}')
    
    for letra in palavra:
        if letra in tentativas:
            print(letra, end = ' ')
        else:
            print('_', end = ' ')
    
    palpite = str(input('\nInforme seu palpite ou saia digitando SAIR: ')).lower()
    if palpite == 'sair':
        break
    elif palpite not in alfabeto or palpite == '':
        print('Digite uma letra do alfabeto.')
    elif palpite in tentativas:
        print('A letra já foi digitada anteriormente.')
    tentativas.append(palpite)
    if palpite in palavra and not set(palavra).issubset(set(tentativas)):
        print('Boa! Acertou a letra.')
    elif palpite not in palavra and not set(palavra).issubset(set(tentativas)):
        print('Essa letra não está na palavra!')
        chances -= 1
    if chances == 0:
        print(f'\033[1;31mVOCÊ PERDEU!\033[m a palavra era {palavra.upper()}')
        break
    elif set(palavra).issubset(set(tentativas)):
        for letra in palavra:
            print(letra, end = ' ')
        print('\nVocê acertou a palavra!')
        print(f'\033[1;32mVOCÊ GANHOU! MEUS PARABÉNS.\033[m')
        break