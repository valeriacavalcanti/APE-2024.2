idades = [0] * 8
soma = 0

# iterar pelos índices do vetor com objetivo de armazenar valores
for i in range(8):
    idades[i] = int(input('Idade: '))
    soma = soma + idades[i]

# calcular a média
media = soma / len(idades)

# iterar pelos índices do vetor com objetivo de exibir os valores armazenados
for i in range(8):
    print(i, idades[i])

# iterar pelos elementos do vetor
for idade in idades:
    print(idade)
