from modulos import *


cor0 = '#fof3f5' # Preta
cor1 = '#feffff' # Branca
cor2 = '#3fb5a3' # verde
cor3 = '#38576b' # azul cinzento
cor4 = '#403d3d' # letra

# Janela
janela = Tk()
janela.title('')
janela.geometry('310x300')
janela.configure(bg = cor1)
janela.resizable(width = False, height = False)

# Frame1
frame1 = Frame(janela, width = 310, height = 50, bg = cor1, relief = 'flat')
frame1.grid(row = 0, column = 0, pady = 1, padx = 0, sticky = NSEW)

# Frame2
frame2 = Frame(janela, width = 310, height = 250, bg = cor1, relief = 'flat')
frame2.grid(row = 1, column = 0, pady = 1, padx = 0, sticky = NSEW)
 
#Configurando Frame1
lb_login = Label(frame1, text = 'LOGIN', anchor = NE, font = ('Ivy 25'), 
            bg = cor1, fg = cor4)
lb_login.place(x = 5, y = 5)

lb_linha = Label(frame1, text = '',width = 275, anchor = NW, font = ('Ivy 1'), 
            bg = cor2, fg = cor4)
lb_linha.place(x = 10, y = 45)

credenciais = ['Caio', '123456']

def verifica_senha():
    nome = entry_nome.get()
    senha = entry_senha.get()
    
    if nome == 'admin' and senha == 'admin':
        messagebox.showinfo('Login', 'Seja bem vindo Admin !!!')
    elif credenciais[0] == nome and credenciais[1] == senha:
        messagebox.showinfo('Login', 'Seja bem vindo de volta Caio !!!')
        
        # Deletar itens presentes nos dois frames
        for widget in frame2.winfo_children():
            widget.destroy()
        for widget in frame1.winfo_children():
            widget.destroy()
            
        nova_janela()
    else:
        messagebox.showwarning('Erro', 'Verificar o nome e a senha')
        
def nova_janela():
    lb_usuario = Label(frame1, text = f'Usuário: {credenciais[0]}', anchor = NE, font = ('Ivy 10'),
                 bg = cor1, fg = cor4)
    lb_usuario.place(x = 10, y = 20)
    
    lb_linha = Label(frame1, text = '',width = 275, anchor = NW, font = ('Ivy 1'), 
            bg = cor2, fg = cor4)
    lb_linha.place(x = 10, y = 45)

    lb_msg = Label(frame2, text = f'Seja bem vindo {credenciais[0]}', anchor = NE, font = ('Ivy 10'),
                 bg = cor1, fg = cor4)
    lb_msg.place(x = 10, y = 20)

#Configurando Frame2
lb_nome = Label(frame2, text = 'Nome *', anchor = NE, font = ('Ivy 10'), bg = cor1, fg = cor4)
lb_nome.place(x = 10, y = 20)
entry_nome = Entry(frame2, width = 25, justify = 'left', font = ('', 15),
             highlightthickness = 1, relief = 'solid')
entry_nome.place(x = 14, y = 50)

lb_senha = Label(frame2, text = 'Senha *', anchor = NE, font = ('Ivy 10'), bg = cor1, fg = cor4)
lb_senha.place(x = 10, y = 95)
entry_senha = Entry(frame2, width = 25, justify = 'left',show = '*', font = ('', 15), 
              highlightthickness = 1, relief = 'solid')
entry_senha.place(x = 14, y = 130)

bt_entrar = Button(frame2, text = 'Entrar', width = 39, height = 2, 
            font = ('Ivy 8 bold'), bg = cor2, fg = cor1, 
            relief = 'raised', overrelief = 'ridge', command = verifica_senha)
bt_entrar.place(x = 15, y = 180)


janela.mainloop()