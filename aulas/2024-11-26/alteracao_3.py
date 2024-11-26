maior_nota = -1
soma = 0
qtd_notas = int(input('Quantidade de notas: '))
for i in range(qtd_notas):
    nota = int(input(f'Nota {i + 1}: '))
    soma = soma + nota
    if nota > maior_nota:
        maior_nota = nota

media = soma / qtd_notas

print(f'Média = {media:.2f}')
print(f'Maior nota = {maior_nota}')

