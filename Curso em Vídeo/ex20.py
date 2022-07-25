def main():
    import random
    a1=input('Primeiro aluno: ')
    a2=input('Segundo aluno: ')
    a3=input('Terceiro aluno: ')
    a4=input('Quarto aluno: ')
    lista_alunos=[a1,a2,a3,a4]
    random.shuffle(lista_alunos)
    print('A sequência de apresentação de trabalhos será\n{}'.format(lista_alunos))
main()