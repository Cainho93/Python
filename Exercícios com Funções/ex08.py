import locale
from datetime import datetime 

locale.setlocale(locale.LC_ALL, 'pt_BR')

def data_ext(data_str):
    try:
        datetime.strptime(data_str, '%d/%m/%Y')
    except ValueError:
        print('Formato de data inválida (DD/MM/AAAA) ou data inexistente')
        return None
    else:
        data_datetime = datetime.strptime(data_str, '%d/%m/%Y')
        return datetime.strftime(data_datetime, '%d de %B de %Y')
    
data = input('Digite uma data no formato DD/MM/AAAA: ')
print_data = data_ext(data)
if print_data is not None:
    print('-' * 20)
    print(print_data)
    print('-' * 20)