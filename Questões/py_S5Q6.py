# Questão 6 da sessão 5

import os
numero = float(input('Digite um número: '))
numero2 = float(input('Digite outro número: '))

while float.is_integer(numero) and float.is_integer(numero2):
    if numero>numero2:
        print(f'O numero {numero} é maior')
        print(f'A diferença é {numero-numero2}')

    else:
        print(f'O numero {numero2} é maior')
        print(f'A diferença é {numero2-numero}')
    numero = float(input('\nDigite um número: '))
    numero2 = float(input('Digite outro número: '))
