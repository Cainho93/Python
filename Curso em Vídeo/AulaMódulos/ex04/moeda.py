def aumentar(n = 0, t = 0, f = False):
    aumento = n + (n * t / 100)
    if f:
        return moeda(aumento)
    return aumento


def diminuir(n = 0, t = 0, f = False):
    diminui = n - (n * t / 100)
    if f:
        return moeda(diminui)
    return diminui

def metade(n = 0, f = False):
    meio = n / 2
    if f:
        return moeda(meio)
    return meio

def dobrar(n = 0, f = False):
    dobro = n * 2
    if f:
        return moeda(dobro)
    return dobro

def triplicar(n = 0, f = False):
    triplo = n * 3
    if f:
        return moeda(triplo)
    return triplo

def moeda(n = 0, moeda = 'R$'):
    return f'{moeda} {n:.2f}'.replace('.', ',')

def resumo(n = 0, a = 10, d = 5):
    print('-' * 35)
    print('REUSMO DO VALOR'.center(35))
    print('-' * 35)
    print(f'Preço analisado: \t{moeda(n)}')
    print(f'Metade do preço: \t{metade(n, True)}')
    print(f'Dobro do preço: \t{dobrar(n, True)}')
    print(f'{a}% de aumento: \t{aumentar(n, a, True)}')
    print(f'{d}% de redução: \t{diminuir(n, d, True)}')
    print('-' * 35)