nome1 = input('Informe o nome da primeira pessoa: ')
idade1 = int(input('Informe a idade da primeira pessoa: '))

nome2 = input('Informe o nome da segunda pessoa: ')
idade2 = int(input('Informe a idade da segunda pessoa: '))

if idade1 > idade2:
    print(f'{nome1} é a pessoa mais velha.')
else:
    print(f'{nome2} é a pessoa mais velha.')
