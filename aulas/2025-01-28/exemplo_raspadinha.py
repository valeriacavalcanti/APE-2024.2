import random

# declarar uma matriz 4x4, com valores 0
matriz = []
for i in range(4):
    matriz.append([0] * 4)


# gerar valores aleatórios e colocar na matriz
for i in range(4):
    for j in range(4):
        matriz[i][j] = random.randint(5,10)


# matriz = [[9, 9, 9, 7], [5, 7, 8, 5], [5, 9, 8, 7], [6, 5, 5, 5]]

# pedir a localização para 16 pessoas
for i in range(16):
    linha = int(input('Linha: '))
    coluna = int(input('Coluna: '))
    print(matriz[linha][coluna])
    matriz[linha][coluna] = 0
    






