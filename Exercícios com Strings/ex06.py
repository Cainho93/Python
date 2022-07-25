data = input('DD/MM/AAAA: ')

lista_data = data.split('/')

meses = ["janeiro", "fevereiro", "março", "abril", "maio","junho", 
"julho", "agosto", "setembro", "outubro","novembro", "dezembro"]

data_extenso = meses[int(lista_data[1]) - 1]

print(f'{lista_data[0]} de {data_extenso.capitalize()} de {lista_data[2]}')