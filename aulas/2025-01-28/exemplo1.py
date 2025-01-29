matriz = []
for i in range(3):
    matriz.append([0] * 4)

# exibir toda a matriz (linearmente)
print(matriz)

# exibir TODAS as posições da matriz
for i in range(3):
    for j in range(4):
        print(i, j, matriz[i][j])
