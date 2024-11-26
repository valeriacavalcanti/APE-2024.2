nota1 = int(input('Nota 1: '))
nota2 = int(input('Nota 2: '))

soma  = nota1 + nota2
media = soma / 2

print(f'Média = {media:.2f}')

if nota1 > nota2:
    print(f'Maior = {nota1}')
else:
    print(f'Maior = {nota2}')

