# Declarar a matriz;
matriz = [[10,20,30,40], [50,60,70,80], [90,100,110,120]]

# Exibir o elemento que está na linha 1 coluna 3;
print(matriz[1][3])

# Alterar o elemento que está na linha 2 coluna 2 para 200;
matriz[2][2] = 200
print(matriz)

# Dobrar o valor dos elementos que estão na linha 2;
for i in range(4):
    matriz[2][i] *= 2
print(matriz)

# Exibir a soma dos elementos que estão na linha 1;
soma = 0
for i in range(4):
    soma += matriz[1][i]
print(soma)

# Exibir a soma dos elementos que estão na coluna 3.
soma = 0
for i in range(3):
    soma += matriz[i][3]
print(soma)

# Calcular a média de todos os elementos da matriz;
soma = 0
for i in range(3):
    for j in range(4):
        soma += matriz[i][j]
media = soma / 12
print(media)

# Adicionar uma linha na matriz com os valores: 130,140,150,160;
matriz.append([130,140,150,160])
print(matriz)

# Calcular a soma dos elementos que estão na
# diagonal principal;
soma = 0
for i in range(4):
    soma += matriz[i][i]
print(soma)


# recalcular a média
soma = 0
for i in range(4):
    for j in range(4):
        soma += matriz[i][j]
media = soma / 16
print(media)


# Calcular a quantidade de elementos da matriz
# que possuem valor acima da média.

qtd_acima = 0
for i in range(4):
    for j in range(4):
        if matriz[i][j] > media:
            qtd_acima += 1
print(qtd_acima)

print(matriz)

