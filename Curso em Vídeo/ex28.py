def main():
    from random import randint
    from time import sleep
    print('Vou pensar em um número de 0 e 5, tente adivinhar.')
    meu_numero=int(input('Digite o número: '))
    num_comp=randint(0,5)
    print('PROCESSANDO...')
    sleep(2)
    if meu_numero==num_comp:
        print('Meus Parabéns. Você ganhou!.')
    elif meu_numero!=num_comp:
        print('Você perdeu!. Meu número foi o {}'.format(num_comp))
main()