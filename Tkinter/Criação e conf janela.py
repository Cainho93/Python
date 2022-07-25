from modulos import * 
from validEntry import Validadores
from frameGrad import GradienteFrame
from Relatórios import Relatorios
from Funcionalidades import Funcs
from PlaceHolder import EntPlaceHolder
import pycep_correios
 
janela = tix.Tk()

class Application(Funcs, Relatorios, Validadores):
    def __init__(self):
        self.janela = janela
        self.validaEntradas()
        self.tela()
        self.frames_da_tela()
        self.widgets_frame_1()
        self.lista_frame_2()
        self.monta_tabelas()
        self.select_lista()
        self.Menus()
        janela.mainloop()
    def cepCorreios(self):
        try:
            self.cidade_entry.delete(0, END)
            self.endereco_entry.delete(0, END)
            self.bairro_entry.delete(0, END)
            zipcode = self.cep_entry.get()
            dadosCEP = pycep_correios.get_address_from_cep(zipcode)
            print(dadosCEP)
            self.cidade_entry.insert(END, dadosCEP['cidade'])
            self.bairro_entry.insert(END, dadosCEP['bairro'])
            self.endereco_entry.insert(END, dadosCEP['logradouro'])
        except:
            messagebox.showinfo('CEP', 'O CEP não foi encontrado')
    def tela(self):
        self.janela.title('Cadastro de Clientes') # Título da janela
        self.janela.configure(background = 'SteelBlue4') # Cor de fundo
        self.janela.geometry('700x500') # Horizontal x Vertical
        self.janela.resizable(True, True) # Responsividade da tela
        self.janela.maxsize(width = 900, height = 700) # Tamanho max da tela
        self.janela.minsize(width = 500, height = 400) # Tamanho min da tela
    def frames_da_tela(self):
        # highlightbackground = cor da borda
        # highlightthickness = tamanho da borda
        self.frame_1 = Frame(self.janela, bd = 4, bg = 'beige',
                highlightbackground = 'SteelBlue2', 
                highlightthickness = 3) # Criando um frame e add borda
        # relx = Movimento horizontal (0 a 1)
        # rely = Movimento vertical (0 a 1)
        # relwidth = Largura do frame
        # relheigth = Altura do frame
        self.frame_1.place(relx = 0.02, rely = 0.02, relwidth = 0.96, relheight = 0.46) # Ajustando o frame
        self.frame_2 = Frame(self.janela, bd = 4, bg = 'beige',
        highlightbackground ='SteelBlue2', highlightthickness = 3)
        self.frame_2.place(relx = 0.02, rely = 0.5, relwidth = 0.96, relheight = 0.46)
    def widgets_frame_1(self):
        # Notebook cria as abas
        self.abas = ttk.Notebook(self.frame_1)
        self.aba1 = GradienteFrame(self.abas, 'lightgray', 'lightblue')
        self.aba2 = Frame(self.abas)
        
        self.aba1.configure(bg = 'beige')
        self.aba2.configure(bg = 'lightgray')
        
        self.abas.add(self.aba1, text = 'Aba 1')
        
        self.abas.add(self.aba2, text = 'Aba 2')
        
        self.abas.place(relx = 0, rely = 0, relwidth = 0.98, relheight = 0.98)
        
        # Colocando cor na aba 1
        self.canvas_bt = Canvas(self.aba1, bd = 0, bg = 'black', highlightbackground = 'gray',
            highlightthickness = 3)
        # Posicionando a aba 1
        self.canvas_bt.place(relx = 0.19, rely = 0.08, relwidth = 0.23, relheight = 0.19)
        
        # Criando o botão limpar
        self.bt_limpar = Button(self.aba1, text = 'Limpar', bd = 2, bg = 'RoyalBlue2',
            fg = 'white', activebackground = 'RoyalBlue1', activeforeground = 'white',
            font = ('verdana', 8, 'bold'), command = self.limpar_cliente)
        self.bt_limpar.place(relx = 0.2, rely = 0.1, relwidth = 0.1, relheight = 0.15)
        self.balao_limpar = tix.Balloon(self.aba1)
        self.balao_limpar.bind_widget(self.bt_limpar,
            balloonmsg = 'Limpe o que foi digitado nos campos')
        
        # Criando o botão buscar
        self.bt_buscar = Button(self.aba1, text = 'Buscar', bd = 2, bg = 'RoyalBlue2',
            fg = 'white', activebackground = 'RoyalBlue1', activeforeground = 'white',
            font = ('verdana', 8, 'bold'), command = self.buscar_cliente)
        self.bt_buscar.place(relx = 0.31, rely = 0.1, relwidth = 0.1, relheight = 0.15)
        self.balao_buscar = tix.Balloon(self.aba1)
        self.balao_buscar.bind_widget(self.bt_buscar, 
            balloonmsg = 'Digite no campo Nome o cliente que deseja pesquisar')
        
        # Criando o botão novo
        self.bt_novo = Button(self.aba1, text = 'Novo', bd = 2, bg = 'RoyalBlue2',
            fg = 'white', activebackground = 'RoyalBlue1', activeforeground = 'white', 
            font = ('verdana', 8, 'bold'), command = self.add_cliente)
        self.bt_novo.place(relx = 0.6, rely = 0.1, relwidth = 0.1, relheight = 0.15)
        self.balao_novo = tix.Balloon(self.aba1)
        self.balao_novo.bind_widget(self.bt_novo,
            balloonmsg = 'Adicione um novo cliente')
        
        # Criando o botão alterar
        self.bt_alterar = Button(self.aba1, text = 'Alterar', bd = 2, bg = 'RoyalBlue2',
            fg = 'white', activebackground = 'RoyalBlue1', activeforeground = 'white', 
            font = ('verdana', 8, 'bold'), command = self.alterar_cliente)
        self.bt_alterar.place(relx = 0.7, rely = 0.1, relwidth = 0.1, relheight = 0.15)
        self.balao_alterar = tix.Balloon(self.aba1)
        self.balao_alterar.bind_widget(self.bt_alterar,
            balloonmsg = 'Altere o valor de qualquer campo selecionado')
        
        # Criando o botão apagar 
        self.bt_apagar = Button(self.aba1, text = 'Apagar', bd = 2, bg = 'RoyalBlue2',
            fg = 'white', activebackground = 'RoyalBlue1', activeforeground = 'white',
            font = ('verdana', 8, 'bold'), command = self.deletar_cliente)
        self.bt_apagar.place(relx = 0.8, rely = 0.1, relwidth = 0.1, relheight = 0.15)
        self.balao_apagar = tix.Balloon(self.aba1)
        self.balao_apagar.bind_widget(self.bt_apagar,
            balloonmsg = 'Apague o cliente selecionado (Clientes apagados não retornam)')
        
        # Criando o botão CEP e a Entry
        self.bt_cep = Button(self.aba1, text = 'CEP', bd = 2, bg = 'Beige',
            fg = 'RoyalBlue2', activeforeground = 'RoyalBlue2', activebackground = 'white',
            font = ('verdana', 10), command = self.cepCorreios)
        self.bt_cep.place(relx = 0.65, rely = 0.35, relwidth = 0.08, relheight = 0.16)
        self.cep_entry = EntPlaceHolder(self.aba1, 'Digite o CEP do cliente')
        self.cep_entry.place(relx = 0.75, rely = 0.35, relwidth = 0.2)
            
        # Criando a Label e a entrada do código 
        self.lb_codigo = Label(self.aba1, text = 'Código', bg = 'beige', fg = 'RoyalBlue2')
        self.lb_codigo.place(relx = 0.05, rely = 0.05)
        self.codigo_entry = EntPlaceHolder(self.aba1, 'Código')
        self.codigo_entry.place(relx = 0.05, rely = 0.15, relwidth = 0.07)
        
        # Criando a Label e a entrada do nome
        self.lb_nome = Label(self.aba1, text = 'Nome', bg = 'beige', fg = 'RoyalBlue2')
        self.lb_nome.place(relx = 0.02, rely = 0.35)
        self.nome_entry = EntPlaceHolder(self.aba1, 'Digite o nome do cliente')
        self.nome_entry.place(relx = 0.09, rely = 0.35, relwidth = 0.5)
        
        # Criando a Label e a entrada do telefone
        self.lb_telefone = Label(self.aba1, text = 'Telefone', bg = 'beige', fg = 'RoyalBlue2')
        self.lb_telefone.place(relx = 0.02, rely = 0.6)
        self.telefone_entry = EntPlaceHolder(self.aba1, 'Digite o telefone do cliente')
        self.telefone_entry.place(relx = 0.11, rely = 0.6, relwidth = 0.3)
        
    
        # Criando a Label e a entrada da cidade
        self.lb_cidade = Label(self.aba1, text = 'Cidade', bg = 'beige', fg = 'RoyalBlue2')
        self.lb_cidade.place(relx = 0.52, rely = 0.6)
        self.cidade_entry = EntPlaceHolder(self.aba1, 'Digite a cidade do cliente')
        self.cidade_entry.place(relx = 0.6, rely = 0.6, relwidth = 0.3)
        
        # Criando Label e a entrada do endereço
        self.lb_endereco = Label(self.aba1, text = 'Endereço', bg = 'beige', fg = 'RoyalBlue2')
        self.lb_endereco.place(relx = 0.02, rely = 0.8)
        self.endereco_entry = EntPlaceHolder(self.aba1, 'Digite o endereço do cliente')
        self.endereco_entry.place(relx = 0.11 , rely = 0.8, relwidth = 0.3)
        
        # Criando Label e a entrada do bairro
        self.lb_bairro = Label(self.aba1, text = 'Bairro', bg = 'beige', fg = 'RoyalBlue2')
        self.lb_bairro.place(relx = 0.52, rely = 0.8)
        self.bairro_entry = EntPlaceHolder(self.aba1, 'Digite o bairro do cliente')
        self.bairro_entry.place(relx = 0.6, rely = 0.8, relwidth = 0.3)
        
        # Drop down button
        self.Tipvar = StringVar()
        self.TipV = ('Solteiro(a)', 'Casado(a)', 'Divorciado(a)', 'Viúvo(a)')
        self.Tipvar.set('Solteiro(a)')
        self.popupMenu = OptionMenu(self.aba2, self.Tipvar, *self.TipV)
        self.popupMenu.place(relx = 0.1, rely = 0.1, relwidth = 0.2, relheight = 0.2)
        self.estado_civil = self.Tipvar.get()
        print(self.estado_civil)
        
        # Criando o calendário
        self.bt_calendario = Button(self.aba2, text = 'Data',
            command = self.calendario)
        self.bt_calendario.place(relx = 0.5, rely = 0.02)
        self.entry_data = Entry(self.aba2, width = 10)
        self.entry_data.place(relx = 0.5, rely = 0.2)   
    def janela2(self):
        # Para a janela2 se abrir é necessário que eu coloque o commando self.janela2 em um botão
        self.janela2 = Toplevel()
        self.janela2.title('Janela 2')
        self.janela2.configure(bg = 'Lightblue')
        self.janela2.geometry('400x200')
        self.janela2.resizable(False, False)
        # Transient quer saber qual a janela principal 
        self.janela2.transient(self.janela1)
        # Focus_Force faz a janela2 aparecer na frente da janela1
        self.janela2.focus_force()
        # Grab_Set impede qualquer ação na janela1
        self.janela2.grab_set()        
    def lista_frame_2(self):
        # Criando a lista
        self.listaFR2 = ttk.Treeview(self.frame_2, height = 3, column = ('col1', 'col2', 'col3', 'col4'))
        self.listaFR2.heading('#0', text = '')
        self.listaFR2.heading('#1', text = 'Código')
        self.listaFR2.heading('#2', text = 'Nome')
        self.listaFR2.heading('#3', text = 'Telefone')
        self.listaFR2.heading('#4', text = 'Cidade')
        
        # Criando o cabeçalho da lista
        self.listaFR2.column('#0', width = 1)
        self.listaFR2.column('#1', width = 50)
        self.listaFR2.column('#2', width = 200)
        self.listaFR2.column('#3', width = 125)
        self.listaFR2.column('#4', width = 125)
        self.listaFR2.place(relx = 0.01, rely = 0.1, relwidth = 0.95, relheight = 0.85)
        
        # Criando a barra de rolagem da lista
        self.barraRol_lista = Scrollbar(self.frame_2, orient = 'vertical')
        self.listaFR2.configure(yscroll = self.barraRol_lista.set)
        self.barraRol_lista.place(relx = 0.96, rely = 0.1, relwidth = 0.04, relheight = 0.85)
        self.listaFR2.bind('<Double-1>', self.ONDoubleClick)
    def Menus(self):
        menubar = Menu(self.janela)
        self.janela.config(menu = menubar)
        filemenu = Menu(menubar)
        filemenu2 = Menu(menubar)
        
        def Quit(): self.janela.destroy()
        # add.cascade serve para criar menubar
        menubar.add_cascade(label = 'Opções', menu = filemenu)
        menubar.add_cascade(label = 'Relatórios', menu = filemenu2)
        
        filemenu.add_command(label = 'Sair', command = Quit)
        filemenu.add_command(label = 'Limpar Cliente', command = self.limpar_cliente) 
        
        filemenu2.add_cascade(label = 'Ficha do Cliente', command = self.gerarRelatorio)                
    def validaEntradas(self):
        self.validador2 = (self.janela.register(self.validador_entry2), '%P')    

Application()   