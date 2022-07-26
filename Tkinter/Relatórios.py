from modulos import *

class Relatorios():
    def printCliente(self):
        webbrowser.open('cliente.pdf')
    def gerarRelatorio(self):
        self.c = canvas.Canvas('cliente.pdf')
        self.codigoRel = self.codigo_entry.get()
        self.nomeRel = self.nome_entry.get()
        self.telefoneRel = self.telefone_entry.get()
        self.cidadeRel = self.cidade_entry.get()
        
        self.c.setFont('Helvetica-Bold', 24)
        self.c.drawString(200, 790, 'Ficha do Cliente')
        
        self.c.setFont('Helvetica-Bold', 18)
        self.c.drawString(50, 700, 'Código: ')
        self.c.drawString(50, 660, 'Nome: ')
        self.c.drawString(50, 630, 'Telefone: ')
        self.c.drawString(50, 600, 'Cidade: ')
        
        self.c.setFont('Helvetica', 18)
        self.c.drawString(150, 700, self.codigoRel)
        self.c.drawString(150, 660, self.nomeRel)
        self.c.drawString(150, 630, self.telefoneRel)
        self.c.drawString(150, 600, self.cidadeRel)

        self.c.rect(20, 550, 550, 1, fill = False, stroke = True)
        
        self.c.showPage()
        self.c.save()
        self.printCliente()