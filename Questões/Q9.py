# Questão 9 da sessão 5

salario = int(input('Digite o seu salário: '))
prestacao = int(input('Digite o valor da prestação: '))

if prestacao>salario*0.2:
    print(f'Empréstimo não concedido.')
else:
    print(f'Empréstimo concedido.')
    