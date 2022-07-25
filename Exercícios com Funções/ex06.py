def ex_9(n):
    return str(n[::-1])
    
num = str(input('Número: ')).strip()
print(f'Número invertido: {ex_9(num)}')