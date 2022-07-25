nome_completo=str(input('Digite seu primeiro nome: ')).strip()
n=nome_completo.split()
print('Prazer em te conhecer!')
print('Seu primeiro nome é {}'.format(n[0])) #Saber o primeiro nome de uma pessoa
print('Seu último nome é {}'.format(n[len(n)-1])) #Saber o último nome de uma pessoa 