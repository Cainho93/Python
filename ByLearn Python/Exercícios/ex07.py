def main():
    num_escolhido=2
    num_magico=int(input('Digite o seu número:'))
    if num_magico > num_escolhido:
        print('Você precisa diminuir seu chute')
    elif num_magico < num_escolhido:
        print('Você precisa aumentar seu chute')
    else:
        print('Você acertou o meu número')
main() 