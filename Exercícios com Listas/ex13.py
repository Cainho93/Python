temp_mes = list()

for t in range(12):
    temp_mes.append(float(input(f'Informe a temperatura média do {t + 1}º mês: ')))
    
meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho', 
'agosto', 'setembro', 'outubro', 'novembro', 'dezembro']

media_temp = sum(temp_mes) / len(temp_mes)
print()
print(f'Média anual de temperatura: {media_temp:.1f}°C')
print('''Temperaturas dos meses superiores a média anual:
''', end = '')
for temp in range(0, len(temp_mes)):
    if temp_mes[temp] > media_temp:
        print(f'[{temp_mes[temp]}°C em {meses[temp].capitalize()}]')