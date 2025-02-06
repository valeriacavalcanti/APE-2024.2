import random

# declarar dois vetores, um para diagonal principal e outro para diagonal secundária
diagonal_principal = [0] * 3
diagonal_secundaria = []


# declarar uma matriz quadrada de ordem 3
matriz = []
for i in range(3):
    matriz.append([0] * 3)


# preencher com valores aleatórios entre 1 e 100
for i in range(3):
    for j in range(3):
        matriz[i][j] = random.randint(1, 100)


# gerar um vetor com os elementos da diagonal principal
for i in range(3):
    for j in range(3):
        if i == j:
            diagonal_principal[i] = matriz[i][j]

#for i in range(3):
#    diagonal_principal[i] = matriz[i][i]


# gerar um vetor com os elementos da diagonal secundária
for i in range(3):
    for j in range(3):
        if (i + j) == 2:
            diagonal_secundaria.append(matriz[i][j])

#diagonal_secundaria = []
#for i in range(3):
#    diagonal_secundaria.append(matriz[i][2-i])













    
