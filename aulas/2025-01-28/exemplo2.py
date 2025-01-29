import random

# declarar uma matriz 4x4, com valores 0
matriz = []
for i in range(4):
    matriz.append([0] * 4)


# gerar valores aleatórios e colocar na matriz
for i in range(4):
    for j in range(4):
        matriz[i][j] = random.randint(5,10)


matriz = [[9, 9, 9, 7], [5, 7, 8, 5], [5, 9, 8, 7], [6, 5, 5, 5]]

# somar os elementos de cada linha
for i in range(4):
    soma = 0
    for j in range(4):
        soma = soma + matriz[i][j]
    print(soma)


# somar os elementos de cada coluna

for j in range(4):
    soma = 0
    for i in range(4):
        soma = soma + matriz[i][j]
    print(soma)







