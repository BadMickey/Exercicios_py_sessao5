# Questão 19 da sessão 5

numero = float(input('Digite um número inteiro: '))

if float.is_integer(numero):
    if numero%3==0 and numero%5!=0:
        print(f'O número {numero} é divisível por 3 e não por 3 e 5.')
    elif numero%5==0 and numero%3!=0:
        print(f'O número {numero} é divisível por 5 e não por 3 e 5.')
    else:
        print(f'O número se divide por 3 e 5')
else:
    print(f'O número não é inteiro.')    
