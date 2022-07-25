from random import choice

def print_forca(forca):
    print(' '.join(forca).upper())
    print('')
    
palavras = ['jogador', 'positivo', 'homenagem', 'chapando', 'veracruz', 'estourado', 'esquece']
sorteada = choice(palavras)
forca = ['_' for i in range(len(sorteada))]
erros = 0
ganhar = False

while erros < 6 and not ganhar:
    print_forca(forca)
    chute = str(input("Digite uma letra: ")).lower()
    
    if chute not in sorteada:
        erros += 1
        print(f'Você errou pela {erros}ª vez. Tente novamente.')
        continue
        
    for pos, let in enumerate(sorteada):
        if let == chute:
            forca[pos] = chute
            
    if '_' not in forca:
        ganhar = True
print()        
if ganhar:
    print("\033[32mYOU WIN!\033[m")
else:
    print("\033[31mGAME OVER!\033[m")
print()
print_forca(forca)