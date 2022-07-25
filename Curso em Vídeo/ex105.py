def notas(* n, sit = False):
    """
    -> Função que mostra as notas do aluno e sua situação por meio de um dicionário
    n = todas as notas do aluno
    sit = (OPCIONAL) mostra a situação decorrente do aluno
    """
    ficha = dict()
    ficha['total de notas'] = len(n)
    ficha['maior nota'] = max(n)
    ficha['menor nota'] = min(n)
    ficha['média'] = sum(n) / len(n)
    if sit:
        if ficha['média'] >= 7:
            ficha['situação'] = 'APROVADO!'
        elif 5.5 <= ficha['média'] <= 6.9:
            ficha['situação'] = 'RECUPERAÇÃO!'
        else:
            ficha['situação'] = 'REPROVADO!'

    return ficha


resp = notas(4.8, 8, 4, 3, sit = True)
print(resp)
help(notas)