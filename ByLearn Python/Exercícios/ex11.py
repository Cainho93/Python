def main():
    
    alunos = ['Caio','Guilherme','Pedro','Enzo']

    notas = [[10,9],[8,6],[7,9],[5,7]]
    
    if(len(alunos) == len(notas)):
        for atual_aluno in range(len(alunos)):
            soma = 0
            for nota in notas[atual_aluno]:
                soma += nota
            media = soma / len(notas[atual_aluno])
            print(f'O aluno {alunos[atual_aluno]} teve a média {media}')
            if media >=7:
                print('- Aluno aprovado!')
            else:
                print('- Aluno reprovado!')                           
main()    