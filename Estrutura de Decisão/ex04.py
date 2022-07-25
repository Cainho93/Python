letra = str(input('Digite uma letra: ')).upper().strip()
if letra not in 'AEIOU':
    print(f'A letra ( {letra.upper()} ) é uma CONSOANTE')
else:
    print(f'A letra ( {letra.upper()} ) é uma VOGAL')