def bananas():
    total_bananas=int(input('Quantas bananas você tem: '))
    return divisao_bananas(total_bananas)

def divisao_bananas(total_bananas):
    bananas=total_bananas/2
    return bananas

bananas_atual=bananas()
print('Depois de dividir as bananas para 2 pessoas, agora você tem ',bananas_atual,'bananas')