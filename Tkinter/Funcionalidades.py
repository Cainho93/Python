from modulos import *

class Funcs():
    def limpar_cliente(self):
        self.codigo_entry.delete(0, END)
        self.nome_entry.delete(0, END)
        self.telefone_entry.delete(0, END)
        self.cidade_entry.delete(0, END)
        self.endereco_entry.delete(0, END)
        self.bairro_entry.delete(0, END)
        self.cep_entry.delete(0, END)
    def conecta_bd(self):
        self.conn = sqlite3.connect('clientes.bd')
        self.cursor = self.conn.cursor(); print('Conectando ao banco de dados')
    def desconecta_bd(self):
        self.conn.close(); print('Desconectando ao banco de dados')
    def monta_tabelas(self):
        self.conecta_bd()
        # Criar tabela
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS clientes (
                cod INTEGER PRIMARY KEY,
                nome_cliente CHAR(40) NOT NULL,
                telefone INTEGER(20),
                cidade INTEGER(40)
            );
        ''')
        self.conn.commit(); print('Banco de dados criado')
        self.desconecta_bd()
    def variaveis(self):
        self.codigo = self.codigo_entry.get()
        self.nome = self.nome_entry.get()
        self.telefone = self.telefone_entry.get()
        self.cidade = self.cidade_entry.get()
    def add_cliente(self):
        self.variaveis()
        if self.nome_entry.get() == '':
            msg = 'Para cadastrar um novo cliente é necessário um nome'
            # Caixa de msg para aviso
            messagebox.showinfo('Cadastro de clientes - Aviso!', msg)
        else:
            self.conecta_bd()
            
            self.cursor.execute(''' INSERT INTO clientes (nome_cliente, telefone, cidade)
                    VALUES (?, ?, ?)''', (self.nome, self.telefone, self.cidade))
            self.conn.commit()
            self.desconecta_bd()
            self.select_lista()
            self.limpar_cliente()
    def select_lista(self):
        self.listaFR2.delete(*self.listaFR2.get_children())
        self.conecta_bd()
        lista = self.cursor.execute(''' SELECT cod, nome_cliente, telefone, cidade FROM clientes
                    ORDER BY nome_cliente ASC; ''')
        for i in lista:
            self.listaFR2.insert('', END, values = i)
        self.desconecta_bd()
    def ONDoubleClick(self, event):
        self.limpar_cliente()
        self.listaFR2.selection()
        
        for n in self.listaFR2.selection():
            col1, col2, col3, col4 = self.listaFR2.item(n, 'values')
            self.codigo_entry.insert(END, col1)
            self.nome_entry.insert(END, col2)
            self.telefone_entry.insert(END, col3)
            self.cidade_entry.insert(END, col4)
    def deletar_cliente(self):
        self.variaveis()
        self.conecta_bd()
        self.cursor.execute(''' DELETE FROM clientes WHERE cod = ? ''', (self.codigo))
        self.conn.commit()
        self.desconecta_bd()        
        self.limpar_cliente()
        self.select_lista()
    def alterar_cliente(self):
        self.variaveis()
        self.conecta_bd()
        self.cursor.execute('''UPDATE clientes SET nome_cliente = ?, telefone = ?, cidade = ? 
                WHERE cod = ? ''', (self.nome, self.telefone, self.cidade, self.codigo))
        self.conn.commit()
        self.desconecta_bd()
        self.select_lista()
        self.limpar_cliente()
    def buscar_cliente(self):
        self.conecta_bd()
        self.listaFR2.delete(*self.listaFR2.get_children())
        self.nome_entry.insert(END, '%')
        nome = self.nome_entry.get()
        self.cursor.execute('''
                SELECT cod, nome_cliente, telefone, cidade FROM clientes 
                WHERE nome_cliente LIKE "%s" ORDER BY nome_cliente ASC''' % nome)
        buscanomeFR2 = self.cursor.fetchall()
        for i in buscanomeFR2:
            self.listaFR2.insert('', END, values = i)
        self.limpar_cliente()
    
        self.desconecta_bd()
    def calendario(self):
        self.calendario1 = Calendar(self.aba2, fg = 'gray', bg = 'blue',
            font = ('Times', '9', 'bold'), locale = 'pt_br')
        self.calendario1.place(relx = 0.5, rely = 0.1)
        self.calData = Button(self.aba2, text = 'Inserir Data',
            command = self.print_cal)
        self.calData.place(relx = 0.55, rely = 0.85, height = 25, width = 100)
    def print_cal(self):
        # get_date pega a informação do calendario desejado
        dataIni = self.calendario1.get_date()
        self.calendario1.destroy()
        self.entry_data.delete(0, END)
        self.entry_data.insert(END, dataIni)
        self.calData.destroy()
