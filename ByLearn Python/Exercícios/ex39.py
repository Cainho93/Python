def media():
    nome_aluno=input('Digite seu nome: ')
    nota1=float(input('Primeira nota: '))
    nota2=float(input('Segunda nota: '))
    return calcular_media(nota1,nota2)

def calcular_media(nota1,nota2):
    media=(nota1 + nota2)/2
    print('Sua média é: ',media)
    return media

def verificar_aprovacao(media):
    if(media >= 7):
        print('Você passou!')
    else:
        print('Você não passou!')

verificar_aprovacao(media())