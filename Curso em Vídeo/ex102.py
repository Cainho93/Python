def fatorial(n, show = False):
    """
    -> Mostrar o fatorial de um número
    n = Número do fatorial
    show = (Opcional) Mostrar ou não a conta
    """
    
    f = 1
    for c in range(n, 0, -1):
        if show:
            print(c, end = '')
            if c > 1:
                print(' x ', end = '')
            else:
                print(' = ', end = '')
        f *= c
    return f

fat = int(input('Digite um número para ver seu fatorial: '))
print(fatorial(fat, show = True))
help(fatorial)