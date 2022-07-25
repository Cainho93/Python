c =('\033[m', # sem cor 0
    '\033[7;30;41m' # vermelho 1
    '\033[7;30;42m' # verde 2
    '\033[7;30;43m' # amarelo 3
    '\033[7;30;44m' # azul 4
    '\033[7;30;45m' # roxo 5
    '\033[7;30m' # branco 6
    )


def ajuda(com):
    titulo(f'Acessando o manual do comando \'{com}\'')
    print(c[5], end = '')
    help(com)
    print(c[0], end = '')
    
    
def titulo(msg, cor = 0):
    tam = len(msg) + 4
    print(c[cor], end = '')
    print('~' * tam)
    print(f'  {msg}')
    print('~' * tam)
    print(c[0], end = '')
    
    

# Programa Principal
comando = ''
while True:
    titulo('SISTEMA DE AJUDA PyHELP', 3)
    comando = str(input("Função ou biblioteca > "))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
titulo('ATÉ LOGO', 4)