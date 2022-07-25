from modulos import *

class Validadores():
    def validador_entry2(self, text):
        if text == '':
            return True
        try:
            value = int(text)
        except ValueError:
            return False
        # Quantos mais 0 eu colocar dps do 100 acrescenta mais um número na entry do codigo
        return 0 <= value <= 100