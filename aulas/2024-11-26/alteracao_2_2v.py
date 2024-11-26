soma = 0
nota = int(input(f'Nota {i + 1}: '))
maior_nota = nota

for i in range(9):
    nota = int(input(f'Nota {i + 1}: '))
    soma = soma + nota
    if nota > maior_nota:
        maior_nota = nota

media = soma / 10

print(f'Média = {media:.2f}')
print(f'Maior nota = {maior_nota}')

