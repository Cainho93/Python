resp = list()
resp.append(int(input('Telefonou para a vítima? [Sim - 1/ Não - 0]: ')))
resp.append(int(input('Esteve no local do crime? [Sim - 1/ Não - 0]: ')))
resp.append(int(input('Mora perto da vítima? [Sim - 1/ Não - 0]: ')))
resp.append(int(input('Devia para a vítima? [Sim - 1/ Não - 0]: ')))
resp.append(int(input('Já trabalhou com a vítima? [Sim - 1/ Não - 0]: ')))

soma_resp = 0

for r in resp:
    soma_resp += r
print()
print('Status: ',end = '')
if soma_resp <= 1:
    print('<INOCENTE>')
elif soma_resp == 2:
    print('<SUSPEITO>')
elif 3 <= soma_resp <= 4:
    print('<CÚMPLICE>')
elif soma_resp == 5:
    print('<ASSASSINO>')