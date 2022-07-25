# Conversor de medidas mais avançado
# Temperatura 
# Massa
# Comprimento
# Armazenamento de Dados
from time import sleep
print('{:=^40}'.format('\033[1mCONVERSOR DE MEDIDAS'))
print('')
print('''\033[1mOpções:\033[m
[ 1 ] Temperatura (Celsius; Fahrenheit; Kelvin)
[ 2 ] Massa (Tonelada; Kilograma; Grama; Miligrama)
[ 3 ] Comprimento (Kilometro; Metro; Centímetro; Milímetro)''')
print('')
opcao = int(input('\033[1mSua opção: '))
print('')
# Temperatura
if opcao == 1:
    print('\033[1;34mConversões de Temperatura\033[m: ')
    print('''    [ 1 ] °Celsius - °Fahrenheit
    [ 2 ] °Celsius - Kelvin
    [ 3 ] °Fahrenheit - °Celsius
    [ 4 ] °Fahrenheit - Kelvin
    [ 5 ] Kelvin - °Celsius
    [ 6 ] Kelvin - °Fahrenheit''')
    print('')
    conversao_temperatura = int(input('\033[1mConversão: '))
    print('')
    temperatura = float(input('\033[1mTemperatura: '))
    print('')
    print('CONVERTENDO TEMPERATURA...')
    sleep(2)
    print('')
    if conversao_temperatura == 1:
        celsius_fahrenheit = (temperatura * 1.8) + 32
        print('°C: {}\n°F: {:.1f}'.format(temperatura, celsius_fahrenheit))
    elif conversao_temperatura == 2:
        celsius_kelvin = temperatura + 273
        print('°C: {}\nK: {:.1f}'.format(temperatura, celsius_kelvin))
    elif conversao_temperatura == 3:
        fahrenheit_celsius = (temperatura - 32) * 5 / 9
        print('°F: {}\n°C: {}'.format(temperatura, fahrenheit_celsius))
    elif conversao_temperatura == 4:
        fahrenheit_kelvin = (temperatura + 459.67) * 5 / 9
        print('°F: {}\n K: {:.3f}'.format(temperatura, fahrenheit_kelvin))
    elif conversao_temperatura == 5:
        kelvin_celsius = temperatura - 273
        print('K: {}\n°C: {:.1f}'.format(temperatura, kelvin_celsius))
    elif conversao_temperatura == 6:
        kelvin_fahrenheit = temperatura * 9 / 5 - 459.67
        print(' K: {}\n°F: {:.1f}'.format(temperatura, kelvin_fahrenheit))
    else:
        print('\033[1;31mERRO!\033[m\n\033[1mTENTE NOVAMENTE.')
# Massa
if opcao == 2:
    print('\033[1;34mConversões de Massa\033[m:')
    print('''    [ 1 ] Tonelada -  Kilograma
    [ 2 ] Tonelada - Grama
    [ 3 ] Tonelada - Miligrama
    [ 4 ] Kilograma - Tonelada
    [ 5 ] Kilograma - Grama
    [ 6 ] Kilograma - Miligrama
    [ 7 ] Grama - Tonelada
    [ 8 ] Grama - Kilograma
    [ 9 ] Grama - Miligrama
    [ 10 ] Miligrama - Tonelada
    [ 11 ] Miligrama - Kilograma
    [ 12 ] Miligrama - Grama''')
    print('')
    conversao_massa = int(input('\033[1mConversão: '))
    print('')
    massa = float(input('\033[1mMassa: '))
    print('')
    print('CONVERTENDO MASSA...')
    sleep(2)
    print('')
    if conversao_massa == 1:
        tonelada_kilograma = massa * 1000
        print('T: {}\nKg: {}'.format(massa, tonelada_kilograma))
    elif conversao_massa == 2:
        tonelada_grama = massa * 1000000
        print('T: {}\ng: {}'.format(massa, tonelada_grama))
    elif conversao_massa == 3:
        tonelada_miligrama = massa * 1000000000
        print('T: {}\nmg: {}'.format(massa, tonelada_miligrama))
    elif conversao_massa == 4:
        kilograma_tonelada = massa / 1000
        print('Kg: {}\nT: {}'.format(massa, kilograma_tonelada))
    elif conversao_massa == 5:
        kilograma_grama = massa * 1000
        print('Kg: {}\ng: {}'.format(massa, kilograma_grama))
    elif conversao_massa == 6:
        kilograma_miligrama = massa * 1000000
        print('Kg: {}\nmg: {}'.format(massa, kilograma_miligrama))
    elif conversao_massa == 7:
        grama_tonelada = massa / 1000000
        print('g: {}\nT: {}'.format(massa, grama_tonelada))
    elif conversao_massa == 8:
        grama_kilograma = massa / 1000
        print('g: {}\nKg: {}'.format(massa, grama_kilograma))
    elif conversao_massa == 9:
        grama_miligrama = massa * 1000
        print('g: {}\nmg: {}'.format(massa, grama_miligrama))
    elif conversao_massa == 10:
        miligrama_tonelada = massa / 1000000000
        print('mg: {}\nT: {}'.format(massa, miligrama_tonelada))
    elif conversao_massa == 11:
        miligrama_kilograma = massa / 1000000
        print('mg: {}\nKg: {}'.format(massa, miligrama_kilograma))
    elif conversao_massa == 12:
        miligrama_grama = massa / 1000
        print('mg: {}\n g: {}'.format(massa, miligrama_grama))
    else:
        print('\033[1;31mERRO!\033[m\n\033[1mTENTE NOVAMENTE.')
# Comprimento
if opcao == 3:
    print('\033[1;34mConversões de Comprimento\033[m:')
    print('''    [ 1 ] Kilometro - Metro
    [ 2 ] Kilometro - Centímetro
    [ 3 ] Kilometro - Milímetro
    [ 4 ] Metro - Kilometro
    [ 5 ] Metro - Centímetro
    [ 6 ] Metro - Milímetro
    [ 7 ] Centímetro - Kilometro
    [ 8 ] Centímetro - Metro
    [ 9 ] Centímetro - Milímetro
    [ 10 ] Milímetro - Kilometro
    [ 11 ] Milímetro - Metro
    [ 12 ] Milímetro - Centímetro''')
    print('')
    conversao_comprimento = int(input('\033[1mConversão: '))
    print('')
    comprimento = float(input('\033[1mComprimento: '))
    print('')
    print('CONVERTENDO COMPRIMENTO...')
    sleep(2)
    print('')
    if conversao_comprimento == 1:
        kilometro_metro = comprimento * 1000
        print('Km: {}\nm: {}'.format(comprimento, kilometro_metro))
    elif conversao_comprimento == 2:
        kilometro_centimetro = comprimento * 100000
        print('Km: {}\ncm: {}'.format(comprimento, kilometro_centimetro))
    elif conversao_comprimento == 3:
        kilometro_milimetro = comprimento * 1000000
        print('Km: {}\nmm: {}'.format(comprimento, kilometro_milimetro))
    elif conversao_comprimento == 4:
        metro_kilometro = comprimento / 1000
        print('m: {}\nKm: {}'.format(comprimento, metro_kilometro))
    elif conversao_comprimento == 5:
        metro_centimetro = comprimento * 100
        print('m: {}\ncm: {}'.format(comprimento, metro_centimetro))
    elif conversao_comprimento == 6:
        metro_milimetro = comprimento * 1000
        print('m: {}\nmm: {}'.format(comprimento, metro_milimetro))
    elif conversao_comprimento == 7:
        centimetro_kilometro = comprimento / 100000
        print('cm: {}\nKm: {}'.format(comprimento, centimetro_kilometro))
    elif conversao_comprimento == 8:
        centimetro_metro = comprimento / 100
        print('cm: {}\nm: {}'.format(comprimento, centimetro_metro))
    elif conversao_comprimento == 9:
        centimetro_milimetro = comprimento * 10
        print('cm: {}\nmm: {}'.format(comprimento, centimetro_milimetro))
    elif conversao_comprimento == 10:
        milimetro_kilometro = comprimento / 1000000
        print('mm:{}\nKm: {}'.format(comprimento, milimetro_kilometro))
    elif conversao_comprimento == 11:
        milimetro_metro = comprimento / 1000
        print('mm: {}\ncm: {}'.format(comprimento, milimetro_metro))
    elif conversao_comprimento == 12:
        milimetro_centimetro = comprimento / 10
        print('mm: {}\ncm: {}'.format(comprimento, milimetro_centimetro))
    else:
        print('\033[1;31mERRO!\033[m\n\033[1mTENTE NOVAMENTE.')
elif opcao != 1 and opcao != 2 and opcao != 3:
    print('\033[1;31mERRO!\033[m\n\033[1mTENTE NOVAMENTE.')