import os 

print('Arquivo atual:', __file__)

print('Nome do arquivo atual:', os.path.basename(__file__))

print('Pasta do arquivo:', os.path.dirname(__file__))

print('Caminho Absoluto do arquivo:', os.path.abspath(__file__))