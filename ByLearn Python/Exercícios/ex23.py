def main():
    nome= input('Digite seu nome: ')
    nota1= float(input('Digite sua primeira nota: '))
    nota2= float(input('Digite sua segunda nota: '))
    media = (nota1 + nota2) / 2
    print(nome)
    print('Sua média é',media)
    if media > 7:
        print('Você está aprovado!')
    else:
        print('Você está reprovado!')
main()