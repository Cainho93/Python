def media():
    nota1=float(input('Digite sua primeira nota: '))
    nota2=float(input('Digite sua segunda nota: '))
    soma = nota1 + nota2
    media= soma / 2
    return media

minha_media = media()
print('A sua média é :',minha_media)