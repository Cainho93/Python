def ex_8(num):
    return len(num)

n = str(input('Número: ')).strip()
print(f'Nesse número existem {ex_8(n)} dígitos')