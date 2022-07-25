import requests
from tkinter import *

# Código principal
def pegar_cotacoes():
    requisicao = requests.get('https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL')
    
    requisicao_dic = requisicao.json()
    
    cotacao_dolar = requisicao_dic['USDBRL']['bid']
    cotacao_euro = requisicao_dic['EURBRL']['bid']
    cotacao_btc = requisicao_dic['BTCBRL']['bid']
    
    texto = f'''
    Dólar: {cotacao_dolar}
    Euro: {cotacao_euro}
    BTC: {cotacao_btc}'''
    
    texto_cotacoes['text'] = texto
    


# Interface Gráfica
janela = Tk()
janela.title('Cotação Atual das Moedas')
janela.geometry('300x220')
janela.configure(background = 'white')

texto_orientacao = Label(janela, text = 'Clique no botão para ver as cotações das moedas', bg = 'white')
texto_orientacao.grid(column = 0, row = 0, padx =10 , pady = 10)

botao = Button(janela, text = 'Buscar cotações USD/EUR/BTC', command = pegar_cotacoes)
botao.grid(column = 0, row = 1, padx = 10, pady = 10)
botao.configure(bg = 'light blue')

texto_cotacoes = Label(janela, text = '', bg = 'white')
texto_cotacoes.grid(column = 0, row = 2, padx = 10, pady = 10)

botao2 = Button(janela, text = 'Sair', bg = 'red', command = janela.destroy)
botao2.grid(column = 0, row = 3, padx = 10, pady = 10)

janela.mainloop()