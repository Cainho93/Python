#Classe Conta Corrente: Crie uma classe para implementar uma conta corrente. 
#A classe deve possuir os seguintes atributos: número da conta, nome do correntista e saldo. 
#Os métodos são os seguintes: alterarNome, depósito e saque; 
#No construtor, saldo é opcional, com valor default zero e os demais atributos são obrigatórios.
class ContaCorrente(object):
    
    def __init__(self,numero_conta, nome_correntista, saldo = 0):
        self.numero_conta = numero_conta
        self.nome_correntista = nome_correntista
        self.saldo = saldo
        
    def AlterarNome(self, novo_nome):
        self.nome_correntista = novo_nome
        return self.nome_correntista
  
    def deposito(self, depositar):
        self.saldo += depositar
        return self.saldo
        
    def saque(self, sacar):
        self.saldo -= sacar
        return self.saque
    
CC1 = ContaCorrente(234, 'Caio Faccioni')
print(CC1.__dict__)
CC1.AlterarNome('Lucas Faccioni')
CC1.deposito(200)
CC1.saque(75)
print(CC1.__dict__)