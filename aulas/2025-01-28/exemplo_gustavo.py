import random

# declarar uma matriz 4x4, com valores 0
matriz = []
for i in range(4):
    matriz.append([0] * 4)

matriz_t = []
for i in range(4):
    matriz_t.append([0] * 4)


qt = 1
# gerar valores aleatórios e colocar na matriz
for i in range(4):
    for j in range(4):
        matriz[i][j] = qt
        qt += 1

# montar a matriz transposta
for i in range(4):
    for j in range(4):
        matriz_t[j][i] = matriz[i][j]

print(matriz)
print(matriz_t)






