# Questão 17 da sessão 5

basemaior = float(input('Digite a base maior: '))
basemenor = float(input('Digite a base menor: '))
altura = float(input('Digite a altura:'))

if basemaior>0 and basemenor>0:
    area=(basemaior+basemenor)*altura/2
    print(f'A area é de {area}')
