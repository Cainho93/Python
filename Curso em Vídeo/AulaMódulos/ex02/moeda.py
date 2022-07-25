def aumentar(n = 0, t = 0):
    aumento = n + (n * t / 100)
    return aumento


def diminuir(n = 0, t = 0):
    diminui = n - (n * t / 100)
    return diminui

def metade(n = 0):
    meio = n / 2
    return meio

def dobrar(n = 0):
    dobro = n * 2
    return dobro

def triplicar(n = 0):
    triplo = n * 3
    return triplo

def moeda(n = 0, moeda = 'R$'):
    return f'{moeda} {n:.2f}'.replace('.', ',')