from tkinter import *
from estiloWidgets.entryPlaceHolder import *
from estiloWidgets.gradienteFrame import *

root = Tk()

gradiente = GradientFrame(root, 'purple', 'blue')
gradiente.pack()
holder = EntPlaceHold(root, 'Digite seu nome')
holder.place(x = 10, y = 10)
root.mainloop()