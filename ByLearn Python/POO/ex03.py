class Carro(object):
    comprado = False
    
    def __init__(self, modelo, ano, estado):
        self.modelo = modelo
        self.ano = ano
        self.estado = estado
    
    def comprar(self):
        if self.comprado:
            print('Você já comprou o carro, não poderá comprar novamente.')
            return 
        self.comprado = True
        print('Você comprou o carro!')
        
    def test_drive(self):
        if not self.comprado:
            print('Você vai começar o test drive!')
            self.liga_desliga(True)
            if self.acelerar():
                print('Você está acelerando o carro.')
            else:
                print('Você não pode acelerar.')
            self.liga_desliga(False)
            print('Você desligou o carro.')
        else:
            print('Você não pode fazer o test drive, porque ja efetuou a compra do carro')
        
    def acelerar(self):
        return self.comprado
        
        
    def dirigir(self):
        if self.comprado:
            print('Vá dirigir!')
            self.liga_desliga(True)
            if self.acelerar:
                print('Você está acelerando o carro.')
            else:
                print('Você não pode acelerar.')
            self.liga_desliga(False)
        else:
            print('Você só pode dirigir depois de comprar o carro.')
        
    def liga_desliga(self, status):
        if status:
            print('Você ligou o carro.')
        else:
            print('Você desligou o carro.')
    
Audi = Carro('Audi R8', '2020', 'Novo')
Mercedes = Carro('Mercedes GLA', '2015', 'Semi-Novo')
Audi.test_drive()
print('-' * 30)
Audi.comprar()
print('-' * 30)
Audi.dirigir()