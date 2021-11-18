# Questão 7 da sessão 5

numero1 = int(input('Digite o primeiro número: '))
numero2 = int(input('Digite o segundo número: '))

if numero1==numero2:
    print(f'Os números são iguais')
else:
    if numero1>numero2:
        print(f'O {numero1} é o maior')
    elif numero2>numero1:
        print(f'O {numero2} é o maior')
