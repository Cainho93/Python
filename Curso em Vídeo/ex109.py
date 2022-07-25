def LeiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO! Digite um número inteiro válido.\033[m')
            continue
        except KeyboardInterrupt:
            print('\n\033[31mO usuário não informou os dados.\033[m')
            return 0
        else:
            return n
        
def LeiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO! Digite um número real válido.\033[m')
            continue
        except KeyboardInterrupt:
            print('\n\033[31mO usuário não informou os dados.\033[m')
            return 0
        else:
            return n
            

inteiro = LeiaInt('Digite um Inteiro: ')
real = LeiaFloat('Digite um Real: ')
print(f'Os valores informados foram {inteiro} e {real}')