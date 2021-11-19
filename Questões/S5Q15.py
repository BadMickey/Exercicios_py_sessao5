# Questão 15 da sessão 5

numerodia = int(input('Digite o número do dia da semana: '))

match numerodia:
    case 1:
        print(f'Domingo.')
    case 2:
        print(f'Segunda-feira')
    case 3:
        print(f'Terça-feira.')
    case 4:
        print(f'Quarta-feira.')
    case 5:
        print(f'Quinta-feira.')
    case 6: 
        print(f'Sexta-feira.')
    case 7:
        print(f'Sábado.')
