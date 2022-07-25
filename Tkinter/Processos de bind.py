from tkinter import *
from tkinter import ttk
janela = Tk()

l = ttk.Label(janela, text = 'Começando...')
l.grid()
l.bind('<Enter>', lambda e: l.configure(text = 'Movido o mouse \n'
                                        'para dentro'))
l.bind('<Leave>', lambda e: l.configure(text = 'Movido o mouse \n'
                                        'para fora'))
l.bind('<1>', lambda e: l.configure(text = 'clicou botão esquerdo do mouse'))
l.bind('<Double-1>', lambda e: l.configure(text = 'Duplo clique'))
l.bind('<B3-Motion>', lambda e: l.configure(text = 'Arraste o botão \n'
                                            'direito para %d, %d' % (e.x, e.y)))

janela.mainloop()