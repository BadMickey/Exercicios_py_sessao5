# Questão 14 da sessão 5

notatrab = float(input('Digite a sua nota do trabalho de laboratório: '))
avsemestral = float(input('Digite a sua nota da avaliação semestral: '))
examfinal = float(input('Digite a sua nota do exame final: '))

if notatrab>=0 and notatrab<=10 and avsemestral>=0 and avsemestral<=10 and examfinal>=0 and examfinal<=10:
    media = (notatrab*2 + avsemestral*3 + examfinal*5)/(2+3+5)
    if media>=0 and media<=2.9:
        print(f'Aluno reprovado com média de {media}')
    elif media>=3 and media<=4.9:
        print(f'Aluno de recuperação com média de {media}')
    else:
        print(f'Aluno aprovado com média de {media}.')
