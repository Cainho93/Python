class Aluno(object):
    
    def __init__(self, nome):
        self.nome = nome
        
    def inserir_notas(self, nota1, nota2):
        try:
            self.nota1 = float(nota1)
            self.nota2 = float(nota2)
        except ValueError:
            print('Digite só números REAIS')
        
    def calcular_media(self):
        try:
            return (self.nota1 + self.nota2) / 2
        except AttributeError:
            print('Você não informou as notas')
    
    def infos(self):
        try:
            if self.calcular_media() >= 6:
                print(f'O aluno {self.nome} foi APROVADO!')
            else:
                print(f'O aluno {self.nome} foi REPROVADO!')
        except TypeError:
            print('Você precisa calcular a média ainda')
            
caio = Aluno('Caio')
caio.inserir_notas('dez', 3.6)