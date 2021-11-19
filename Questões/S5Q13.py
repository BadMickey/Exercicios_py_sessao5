# Questão 13 da sessão 5

nota1 = float(input('Digite a nota 1: '))
nota2 = float(input('Digite a nota 2: '))
nota3 = float(input('Digite a nota 3: '))
media = (nota1*1 + nota2*1 + nota3*2)/(1+1+2)

if media>=6.0:
    print(f'Aluno aprovado com a media de {media} pts.')
else:
    print(f'Aluno reprovado com a media de {media} pts.')
