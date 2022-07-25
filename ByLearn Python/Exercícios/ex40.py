#Exercicio de subtraçao
def bolinhas():
    bolinhas_caio=int(input('Quantas bolinhas você tem: '))
    bolinhasp_caio=int(input('Quantas bolinhas você perdeu: '))
    return subtracao_bolinhas(bolinhas_caio,bolinhasp_caio)

def subtracao_bolinhas(bolinhas_caio,bolinhasp_caio):
    bolinhas=(bolinhas_caio-bolinhasp_caio)
    return bolinhas

quantidade_atual_bolinhas=bolinhas()
print('Você perdeu',quantidade_atual_bolinhas,'bolinhas')