times = ('Corinthians', 'Palmeiras', 'Santos', 'Grêmio', 'Cruzeiro', 'Flamengo', 'Vasco da Gama', 
         'Chapecoense', 'Atlético - MG', 'Botafogo', 'Atlético - PR', 
         'Bahia', 'São Paulo', 'Fluminense', 'Sport Recife', 'EC Vitória',
         'Coritiba', 'Avaí', 'Ponte Preta', 'Atlético - GO')

print('-=' * 30)
print(f'\033[1mA lista de times do Brasileirão 2017\033[m: {times}')
print('-=' * 30)
print(f'\033[1mOs 5 primeiros são\033[m {times[0:5]}')
print('-=' * 30)
print(f'\033[1mOs 4 últimos são\033[m {times[16:20]}')
print('-=' * 30)
print(f'\033[1mTimes em ordem alfabética\033[m: {sorted(times)}')
print('-=' * 30)
print(f'A Chapecoense está na {times.index("Chapecoense") + 1}ª posição')