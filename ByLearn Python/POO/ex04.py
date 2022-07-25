class Calculadora(object):
    
    def somar(self, primeiro_valor, segundo_valor):
        return primeiro_valor + segundo_valor
    
    def subtrair(self, primeiro_valor, segundo_valor):
        return primeiro_valor - segundo_valor
    
    def multiplicacao(self, primeiro_valor, segundo_valor):
        return primeiro_valor * segundo_valor
    
    def divisao(self, primeiro_valor, segundo_valor):
        return primeiro_valor / segundo_valor
    
pv = float(input('Digite um valor: '))
sv = float(input('Digite outro valor: '))

calc = Calculadora()
calc.multiplicacao(pv, sv)