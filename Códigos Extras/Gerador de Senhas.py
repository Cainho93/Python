import random 
from string import digits, punctuation, ascii_letters

symbols = ascii_letters + digits + punctuation
secure_random = random.SystemRandom()
password = ''.join(secure_random.choice(symbols) for i in range(15))
print('=' * 30)
print(f'Senha Gerada: {password}')
print('=' * 30)