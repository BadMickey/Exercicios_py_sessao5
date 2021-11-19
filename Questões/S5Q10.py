# Questão 10 da sessão 5

altura = float(input('Digite a sua altura: '))
sexo = input('Digite qual o seu sexo:')

if sexo=='Homem' or sexo=='homem':
    pesoideal=(72.7*altura)-58
    print(f'O peso ideal do homem é {pesoideal}')
elif sexo=='Mulher' or sexo=='mulher':
    pesoideal=(62.1*altura)-44.7
    print(f'O peso ideal do homem é {pesoideal}')
    