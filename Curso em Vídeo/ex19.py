def main():
    from random import choice
    a1=input('Primeiro aluno: ')
    a2=input('Segundo aluno: ')
    a3=input('Terceiro aluno: ')
    a4=input('Quarto aluno: ')
    lista_alunos=[a1,a2,a3,a4]
    aluno_escolhido=choice(lista_alunos)
    print('O aluno escolhido foi {}'.format(aluno_escolhido))
main()