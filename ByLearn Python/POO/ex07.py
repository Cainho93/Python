#Aprimore a classe do exercício anterior para adicionar o método aumentarSalario (porcentualDeAumento) 
#que aumente o salário do funcionário em uma certa porcentagem.
class Funcionario(object):
    
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario
    
    def nome_func(self):
        print(f'O nome do funcionário é {self.nome}')
        
    def salario_func(self):
        print(f'O funcionário {self.nome} recebe R${self.salario:.2f}')
        
    def AumentarSalario(self, aumento):
        self.aumento = self.salario + (self.salario * aumento / 100)
        print(f'''Com o aumento salarial de {aumento}%: 
O salário de R${self.salario:.2f} passa a ser R${self.aumento:.2f}''')

func = Funcionario('Lucas', 3400.50)
func.nome_func()
func.salario_func()
func.AumentarSalario(7)