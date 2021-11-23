# Questão 11 da sessão 5

numero = int(input('Digite um número: '))
soma = 0

while numero>0:
    soma+=numero%10
    numero=numero//10
print(soma)
