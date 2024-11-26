maior_nota = -1
soma = 0
for i in range(10):
    nota = int(input(f'Nota {i + 1}: '))
    soma = soma + nota
    if nota > maior_nota:
        maior_nota = nota

media = soma / 10

print(f'Média = {media:.2f}')
print(f'Maior nota = {maior_nota}')

