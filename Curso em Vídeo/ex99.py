from time import sleep
def maior(* num):
    cont = mai = 0
    print('-=' * 24)
    print('Analisando os valores passados...')
    for n in num:
        sleep(0.4)
        print(f'{n}', end = ' ')
        sleep(0.4)
        if cont == 0:
            mai = n
        else:
            if n > mai:
                mai = n
        cont += 1
    print(f'Foram informados {cont} valores ao todo.')
    print(f'O maior valor informado foi {mai}')
    sleep(1.5)
          
maior(3, 5, 2, 7, 0)
maior(8, 4, 6)
maior(5, 2)
maior(9)
maior()
print('-=' * 24)