# Funçoes do Caixa Eletrônico:
    # Depósito, Saque e Consulta
# Verificações:
    # Cartão:
        # Se inserido continua 
        # Se não inserido para
    # Sacar valor disponível na conta
    
from time import sleep
from tabulate import tabulate 

def skip():
    print('')
    
def linha(design):
    print(f'{design}' * 45)
    
def loading(msg):
    sleep(0.8)
    print(msg, end = '')
    print('.', end = '')
    sleep(0.8)
    print('.', end = '')
    sleep(0.8)
    print('.')
    sleep(1)
    
class CaixaEletronico:  

    def __init__(self, saldo = 0):
        self.saldo = saldo
        self.operacoes = []
    
    def deposito(self, depositar):
        if depositar % 5 == 0:
            self.saldo += depositar
            self.operacoes.append(['DEPÓSITO', depositar])
            print(f'Depósito de R$ {depositar} realizado.')
        else:
            print('DEPÓSITO NEGADO.')
            print('NOTAS ACEITAS: [ 5 ] [ 10 ] [ 20 ] [ 50 ]')

    def saque(self, sacar):
        if sacar <= self.saldo:
            if sacar % 5 == 0:
                self.saldo -= sacar
                self.operacoes.append(['SAQUE', sacar])
                print(f'Saque de R$ {sacar} realizado.')
            else:
                print('SAQUE NEGADO.')
                print('NOTAS DISPONÍVEIS: [ 5 ] [ 10 ] [ 20 ] [ 50 ]')
        else:
            print('SAQUE NEGADO. <SALDO INSUFICIENTE>')
            
    def extrato(self):
        print('EXTRATO BANCÁRIO')
        skip()
        print(tabulate(self.operacoes, headers = ["OPERAÇÃO", "VALOR EM R$"]))
        skip()
        botao = str(input('Pressione ENTER para voltar ao menu:')).split()
        while botao not in '':
            botao = str(input('Pressione ENTER para voltar ao menu: ')).split()
        if botao == '':
            self.menu          
            
    def menu(self):
        linha('=')
        print(f'''
    [ 1 ] DEPOSITAR
    [ 2 ] SACAR
    [ 3 ] EXTRATO 
    [ 4 ] ENCERRAR PROGRAMA
    
    SALDO: R$ {self.saldo}
        ''')
        linha('=')
        try:
            linha('~')
            opcao = int(input('Selecione sua opção: '))
            linha('~')
            linha('-')
            if opcao == 1:
                loading('ÁREA DE DEPÓSITO')
                skip()
                try:
                    depositar = int(input('Valor de depósito: R$ '))
                    self.deposito(depositar)
                except ValueError:
                    linha('-')
                    print('Valor Inválido!')
                    linha('-')
            elif opcao == 2:
                loading('ÁREA DE SAQUE')
                skip()
                try:
                    sacar = int(input('Valor de saque: R$ '))
                    self.saque(sacar)
                except ValueError:
                    print('Valor Inválido!')
            elif opcao == 3:
                loading('CONSULTANDO EXTRATO')
                skip()
                self.extrato()
            elif opcao == 4:
                print('OPERAÇÃO FINALIZADA.')
                linha('-')
                exit()
            else:
                print('Opção Inválida!')
            linha('-')
        except ValueError:
            linha('-')
            print('Opção Inválida!')
            linha('-')
            
        
             
#############################################################################################  


Bradesco = CaixaEletronico()

try:
    cartao = str(input('Cartão Inserido? [S/N]: ')).strip().upper()[0]
    while True:
        linha('=')
        if cartao not in 'SN':
            cartao = str(input('Cartão Inserido? [S/N]: ')).strip().upper()[0]
        elif cartao in 'S':
            loading('CARREGANDO MENU')
            linha('=')
            Bradesco.menu()
        else:
            print('ACESSO NEGADO!')
            print('OPERAÇÃO FINALIZADA.')
            linha('=')
            break
except IndexError:
    linha('-')
    print('Responda Sim (S) ou Não (N).')
    print('OPERAÇÃO FINALIZADA.')
    linha('-')
