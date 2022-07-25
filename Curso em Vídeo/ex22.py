nome_completo=str(input('Digite seu nome completo: ')).strip()
print(nome_completo.upper())
print(nome_completo.lower())
print(len(nome_completo)-nome_completo.count(' ')) #Quantas letras o nome completo tem sem contar os espaços
print(nome_completo.find(' ')) #Quantas letras tem o primeiro nome/Achar a posição de uma determinada letra dentro dos ('')