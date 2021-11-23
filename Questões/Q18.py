# Questão 18 da sessão 5
from time import sleep

print('As opções são:\n1 - soma\n2 - subtração\n3 - multiplicação\n4 - divisão\n5 - sair')
opcao = int(input('Digite sua opção: '))   

while opcao <= 5:
    match opcao:
        case 1:
            numero1 = int(input('Digite o número 1: '))
            numero2 = int(input('Digite o número 2: '))
            soma = numero1+numero2
            print(f'O resultado da soma é {soma}')
            confirmar = int(input('Digite 1 para continuar em soma e 2 para menu novamente: '))
            if confirmar==1:
                sleep(3)
                print('\n'*130)
            elif confirmar==2:
                print(f'Voltando ao menu.') 
                sleep(6)
                print('\n'*130)
                print(f'As opções são:\n1 - soma\n2 - subtração\n3 - multiplicação\n4 - divisão\n5 - sair')
                opcao = int(input('Digite sua opção: '))   
            else:
                print(f'Opção incorreta, tente novamente.')
                print(f'As opções são:\n1 - soma\n2 - subtração\n3 - multiplicação\n4 - divisão\n5 - sair')
                opcao = int(input('Digite sua opção: '))   
        case 2:
            numero1 = int(input('Digite o número 1: '))
            numero2 = int(input('Digite o número 2: '))
            subtracao = numero1-numero2
            print(f'O resultado da subtração é {subtracao}\nVoltando ao menu.')
            confirmar = int(input('Digite 1 para continuar em subtração e 2 para menu novamente: '))
            if confirmar==1:   
                sleep(3)
                print('\n'*130)
            elif confirmar==2:
                print(f'Voltando ao menu.') 
                sleep(6)
                print('\n'*130)
                print(f'As opções são:\n1 - soma\n2 - subtração\n3 - multiplicação\n4 - divisão\n5 - sair')
                opcao = int(input('Digite sua opção: '))   
            else:
                print(f'Opção incorreta, tente novamente.')
                print(f'As opções são:\n1 - soma\n2 - subtração\n3 - multiplicação\n4 - divisão\n5 - sair')
                opcao = int(input('Digite sua opção: ')) 
 
        case 3:
            numero1 = int(input('Digite o número 1: '))
            numero2 = int(input('Digite o número 2: '))
            multiplicacao = numero1*numero2
            print(f'O resultado da subtração é {multiplicacao}\nVoltando ao menu.')
            confirmar = int(input('Digite 1 para continuar em multiplicação e 2 para menu novamente: '))
            if confirmar==1:   
                sleep(3)
                print('\n'*130)
            elif confirmar==2:
                print(f'Voltando ao menu.') 
                sleep(6)
                print('\n'*130)
                print(f'As opções são:\n1 - soma\n2 - subtração\n3 - multiplicação\n4 - divisão\n5 - sair')
                opcao = int(input('Digite sua opção: '))   
            else:
                print(f'Opção incorreta, tente novamente.')
                print(f'As opções são:\n1 - soma\n2 - subtração\n3 - multiplicação\n4 - divisão\n5 - sair')
                opcao = int(input('Digite sua opção: ')) 
        case 4:
            numero1 = int(input('Digite o número 1: '))
            numero2 = int(input('Digite o número 2: '))
            divisao = numero1/numero2
            print(f'O resultado da subtração é {divisao}\nVoltando ao menu.')
            confirmar = int(input('Digite 1 para continuar em divisão e 2 para menu novamente: '))
            if confirmar==1:   
                sleep(3)
                print('\n'*130)
            elif confirmar==2:
                print(f'Voltando ao menu.') 
                sleep(6)
                print('\n'*130)
                print(f'As opções são:\n1 - soma\n2 - subtração\n3 - multiplicação\n4 - divisão\n5 - sair')
                opcao = int(input('Digite sua opção: '))   
            else:
                print(f'Opção incorreta, tente novamente.')
                print(f'As opções são:\n1 - soma\n2 - subtração\n3 - multiplicação\n4 - divisão\n5 - sair')
                opcao = int(input('Digite sua opção: ')) 
        case 5:
            print(f'Finalizando programa.')
            break
