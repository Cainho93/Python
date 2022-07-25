class Carro(object):
    def __init__(self, nome_carro, estado_carro):
        self.nome_carro = nome_carro
        self.estado_carro = estado_carro
    
    def info(self):
        print(f'O {self.nome_carro} tem o estado {self.estado_carro}')
        
        
bmw = Carro('BMW','usado')
focus = Carro('Focus', 'semi-novo')
audi = Carro('Audi', 'novo')
bmw.info()
focus.info()
audi.info()