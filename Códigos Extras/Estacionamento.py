carros = dict()

def add_carros():
    modelo = str(input('Modelo: ')).capitalize()
    while len(modelo) <= 1:
        modelo = str(input('Modelo: ')).capitalize()
    placa = str(input('Placa: '))
    while len(placa) < 8:
        placa = str(input('Placa: '))
    else:
        carros.update({modelo : placa})
def mostrar_carros():
    if len(carros) == 0:
            print('Não tem nenhum carro registrado')
    else:
        for modelo, placa in carros.items():
            print(f'''
            Modelo: {modelo.capitalize()}
            Placa: {placa.upper()}
            ''')
def saida_carros():
    carro = str(input('Modelo do carro: ')).capitalize()
    while carro not in carros:
        carro = str(input('Modelo do carro: ')).capitalize()
    else:
        print(f'{carro.capitalize()} deletado')    
        del(carros[str(carro)])
def loading():
    from time import sleep
    sleep(0.5)
       
while True:
    loading()
    print(f'''
          [1] Adicionar carro
          [2] Mostrar carro(s)
          [3] Saída de carro
          [4] Encerrar programa
          ''')
    opcao = 0
    try:
        opcao = int(input('Opção: '))
    except ValueError:
        print('Selecione uma opção válida')
    loading()    
    if opcao == 1:
        add_carros()
    elif opcao == 2:
        mostrar_carros()
    elif opcao == 3:
        saida_carros()
    elif opcao == 4:
        print('Encerrando o programa')
        break
    else:
        print('ERRO! Selecione novamente sua opção') 