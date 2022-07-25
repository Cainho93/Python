from forex_python.converter import CurrencyRates
from time import sleep
from datetime import datetime

hora_atual = datetime.now().strftime('%H:%M')
a = ('=' * 27)

while True:
    sleep(1)
    print('''
\033[1mCONVERSOR DE MOEDAS\033[m

    [ 1 ] Real
    [ 2 ] Dólar
    [ 3 ] Euro
    [ 4 ] Libra 
    [ 5 ] Sair do Programa
    ''')
    
    opcao_moeda = int(input('Moeda para conversão ou "5" para sair do programa: '))
    sleep(0.8)
    # Criando o conversor de moedas
    conversor = CurrencyRates()
    
    # Criando a opção do Real
    while opcao_moeda == 1:
        sleep(1)
        print('''
    [ 1 ] Real -> Dólar
    [ 2 ] Real -> Euro
    [ 3 ] Real -> Libra 
    [ 4 ] Voltar ao Menu
    ''')
        
        opcao_conversao = int(input('Esolha a sua conversão: '))
        
        if opcao_conversao == 1:
            valor = float(input('\nValor de conversão: R$ '))
            sleep(0.6)
            real_dolar = round(conversor.convert('BRL', 'USD', valor), 2)
            print(a)
            print(f'Horário: {hora_atual}')
            print(f'R$ {valor:.2f} -> U$ {real_dolar:.2f}')
            print(a)
        elif opcao_conversao == 2:
            valor = float(input('\nValor de conversão: R$ '))
            sleep(0.6)
            real_euro = round(conversor.convert('BRL', 'EUR', valor), 2)
            print(a)
            print(f'Horário: {hora_atual}')
            print(f'R$ {valor:.2f} -> € {real_euro:.2f}')
            print(a)
        elif opcao_conversao == 3:
            valor = float(input('\nValor de conversão: R$ '))
            sleep(0.6)
            real_libra = round(conversor.convert('BRL', 'GBP', valor), 2)
            print(a)
            print(f'Horário: {hora_atual}')
            print(f'R$ {valor:.2f} -> £ {real_libra:.2f}')
            print(a)
        elif opcao_conversao == 4:
            break
    # Criando a opção do Dólar
    while opcao_moeda == 2:
        sleep(1)
        print('''
    [ 1 ] Dólar -> Real
    [ 2 ] Dólar -> Euro
    [ 3 ] Dólar -> Libra 
    [ 4 ] Voltar ao Menu
    ''')

        opcao_conversao = int(input('Escolha a sua conversão: '))
        sleep(1)
        if opcao_conversao == 1:
            valor = float(input('\nValor de conversão: U$ '))
            sleep(0.6)
            dolar_real = round(conversor.convert('USD', 'BRL', valor), 2)
            print(a)
            print(f'Horário: {hora_atual}')
            print(f'U$ {valor:.2f} -> R$ {dolar_real:.2f}')
            print(a)
        elif opcao_conversao == 2:
            valor = float(input('\nValor de conversão: U$ '))
            sleep(0.6)
            dolar_euro = round(conversor.convert('USD', 'EUR', valor), 2)
            print(a)
            print(f'Horário: {hora_atual}') 
            print(f'U$ {valor:.2f} -> € {dolar_euro:.2f}')
            print(a)
        elif opcao_conversao == 3:
            valor = float(input('\nValor de conversão: U$ '))
            sleep(0.6)
            dolar_libra = round(conversor.convert('USD', 'GBP', valor), 2)
            print(a)
            print(f'Horário: {hora_atual}') 
            print(f'U$ {valor:.2f} -> £ {dolar_libra:.2f}')
            print(a)
        elif opcao_conversao == 4:
            break
    # Criando a opção do Euro 
    while opcao_moeda == 3:
        sleep(1)
        print('''
    [ 1 ] Euro -> Real
    [ 2 ] Euro -> Dólar
    [ 3 ] Euro -> Libra 
    [ 4 ] Voltar ao Menu
    ''')  
        
        opcao_conversao = int(input('Escolha a sua conversão: '))
    
        if opcao_conversao == 1:
            valor = float(input('\nValor de conversão: € '))
            sleep(0.6)
            euro_real = round(conversor.convert('EUR', 'BRL', valor), 2)
            print(a)
            print(f'Horário: {hora_atual}')
            print(f'€ {valor:.2f} -> R$ {euro_real:.2f}')
            print(a)
        elif opcao_conversao == 2:
            valor = float(input('\nValor de conversão: € '))
            sleep(0.6)
            euro_dolar = round(conversor.convert('EUR', 'USD', valor), 2)
            print(a)
            print(f'Horário: {hora_atual}')
            print(f'€ {valor} -> U$ {euro_dolar}')
            print(a)
        elif opcao_conversao == 3:
            valor = float(input('\nValor de conversão: € '))
            sleep(0.6)
            euro_libra = round(conversor.convert('EUR', 'GBP', valor), 2)
            print(a)
            print(f'Horário: {hora_atual}')
            print(f'€ {valor:.2f} -> £ {euro_libra:.2f}')
            print(a)
        elif opcao_conversao == 4:
            break
    # Criando a opção da Libra 
    while opcao_moeda == 4:
        sleep(1)
        print('''
    [ 1 ] Libra -> Real
    [ 2 ] Libra -> Dólar
    [ 3 ] Libra -> Euro
    [ 4 ] Voltar ao Menu
    ''')
        
        opcao_conversao = int(input('Escolha a sua conversão: '))
        
        if opcao_conversao == 1:
            valor = float(input('\nValor de conversão: £ '))
            sleep(0.6)
            libra_real = round(conversor.convert('GBP', 'BRL', valor), 2)
            print(a)
            print(f'Horário: {hora_atual}')
            print(f'£ {valor:.2f} -> R$ {libra_real:.2f}')
            print(a)
        elif opcao_conversao == 2:
            valor = float(input('\nValor de conversão: £ '))
            sleep(0.6)
            libra_dolar = round(conversor.convert('GBP', 'USD', valor), 2)
            print(a)
            print(f'Horário: {hora_atual}')
            print(f'£ {valor:.2f} -> U$ {libra_dolar:.2f}')
            print(a)
        elif opcao_conversao == 3:
            valor = float(input('\nValor de conversão: £ '))
            sleep(0.6)
            libra_euro = round(conversor.convert('GBP', 'EUR', valor), 2)
            print(a)
            print(f'Horário: {hora_atual}')
            print(f'£ {valor:.2f} -> € {libra_euro:.2f}')
            print(a)
        elif opcao_conversao == 4:
            break
            
    if opcao_moeda == 5:
        break
    elif opcao_moeda > 5:
        print('\033[1;31mERRO!\033[m OPÇÃO NÃO ENCONTRADA.')