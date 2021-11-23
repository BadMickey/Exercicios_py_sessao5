# Questão 12 da sessão 5
import math

numero = int(input('Digite um número: '))

if numero<0:
    print(f'Número inválido.')
else:
    print(f'O logaritmo do {numero} é {math.log(numero)}')
    