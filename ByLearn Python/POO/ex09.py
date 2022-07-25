class Calculadora(object):
    
    def somar(self, primeiro_valor, segundo_valor):
        return primeiro_valor + segundo_valor
    
    def subtrair(self, primeiro_valor, segundo_valor):
        return primeiro_valor - segundo_valor
    
    def multiplicacao(self, primeiro_valor, segundo_valor):
        return primeiro_valor * segundo_valor
    
    def divisao(self, primeiro_valor, segundo_valor):
        try:
            return primeiro_valor / segundo_valor
        except ZeroDivisionError:
            print("Só faça divisão com números inteiros diferentes de zero")
            
calc = Calculadora()
calc.divisao(3, 2)