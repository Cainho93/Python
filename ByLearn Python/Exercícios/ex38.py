def media():
    nota1=float(input('Digite a primeira nota: '))
    nota2=float(input('Digite a segunda nota: '))
    return calcular_media(nota1,nota2)
    
def calcular_media(nota1,nota2):
    media=(nota1 + nota2)/2
    return media

minha_media=media()
print('A minha média é: ',minha_media)