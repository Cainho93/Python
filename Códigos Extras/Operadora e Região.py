import phonenumbers
from phonenumbers import geocoder, carrier

NumeroDeTelefone = phonenumbers.parse('+5511985307582')

Operadora = carrier.name_for_number(NumeroDeTelefone, 'pt-br')

Regiao = geocoder.description_for_number(NumeroDeTelefone, 'pt-br')

print('=' * 25)
print(f'A operadora é: {Operadora}')
print(f'O estado é: {Regiao}')
print('=' * 25)