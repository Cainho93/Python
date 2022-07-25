#Classe Funcionário: Implemente a classe Funcionário. Um empregado tem um nome (um string) e um salário(um double). 
#Escreva um construtor com dois parâmetros (nome e salário) e métodos para devolver nome e salário. 
#Escreva um pequeno programa que teste sua classe.
class Funcionario(object):
    
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario
    
    def nome_func(self):
        print(f'O nome do funcionário é {self.nome}')
    
    def salario_func(self):
        print(f'O funcionário {self.nome} recebe R${self.salario}')
        
func = Funcionario('Jorge', 2500)
func.nome_func()
func.salario_func()