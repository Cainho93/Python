from ferramentas import *

janela = Tk()
janela.title('Caixa Eletrônico')
janela.configure(bg = 'gainsboro')
janela.geometry('380x390')
janela.resizable(True, True)

# INSTRUÇÕES DO PLACE

# relx = Movimento horizontal (0 a 1)
# rely = Movimento vertical (0 a 1)
# relwidth = Largura do frame (0 a 1)
# relheigth = Altura do frame (0 a 1)

# Frames
#===========================================================

frame_login = Frame(janela, bg = 'blue')
frame_login.place(relx = 0, rely = 0,
relheight = 0.18, relwidth = 1)

frame_info = Frame(janela, bg = 'red')
frame_info.place(relx = 0, rely = 0.18,
relheight = 0.82, relwidth = 1)

#===========================================================

# Labels
#===========================================================

lb_login = Label(frame_login, text = 'LOGIN', bg = 'blue',
fg = 'black', font = ('Ivy 25'))
lb_login.place(relx = 0.05, rely = 0.2) 


janela.mainloop()