from tkinter import * 
from tkinter import ttk
import time

janela = Tk()
janela.title('Barra de Progreso')
janela.geometry('500x400')

def step():
    #barra1['value'] = 10
    #barra1.start(10)
    for x in range(10):
        barra1['value'] += 10
        janela.update_idletasks()
        time.sleep(1)
    
def stop():
    barra1.stop()
    
# Mode = Determinate e Indeterminate
barra1 = ttk.Progressbar(janela, orient = HORIZONTAL, length = 300, mode = 'determinate')
barra1.pack(pady = 20)

botao = Button(janela, text = 'Progresso', command = step)
botao.pack(pady = 20)

botao2 = Button(janela, text = 'Parar', command = stop)
botao2.pack(pady = 20)

janela.mainloop()