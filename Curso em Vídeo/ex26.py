texto=str(input('Digite uma frase: ')).upper().strip() #Pode-se usar mais de uma vez na mesma linha[exemplo:.upper().strip()]
print('A letra A aparece {} vezes'.format(texto.count('A')))
print('A primeira letra A apareceu na posição {} ou índice {}'.format(texto.find('A')+1,texto.find('A')))
#find=Quantas letras tem o primeiro nome/Achar a posição de uma determinada letra dentro dos ('')
print('A última letra A apareceu na posição {} ou índice {}'.format(texto.rfind('A')+1,texto.rfind('A')))