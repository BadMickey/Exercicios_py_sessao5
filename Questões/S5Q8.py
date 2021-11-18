# Questão 8 da sessão 5

nota1 = float(input('Digite a nota 1: '))
nota2 = float(input('Digite a nota 2: '))

if nota1>0 and nota1<=10 and nota2>0 and nota2<=10:
    print(f'As notas são válidas')
    media = nota1+nota2/2
    print(f'A média das notas é de {media}')
else:
    print(f'Uma ou mais notas são inválidas.')
