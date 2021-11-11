# Questão 5 da sessão 5

numero = float(input('Digite um número: '))

while float.is_integer(numero):
    if numero%2==0:
        print(f'O numero {numero} é par')
        numero = float(input('Digite um número: '))
    else:
        print(f'O numero {numero} é impar')
        break
else:
    print('Número inválido por não ser inteiro')
