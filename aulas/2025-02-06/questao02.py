import random

# declarar matriz 20 x 50
matriz = []
for i in range(20):
    matriz.append([0] * 50)

# preencher a matriz com valores aleatorios (1,10)
for i in range(20):
    for j in range(50):
        matriz[i][j] = random.randint(1, 100)

# ler valor inteiro "k"
k = int(input('Digite o valor de k: '))

# procurar "k" e exibir a posição onde encontrei
for i in range(20):
    for j in range(50):
        if matriz[i][j] == k:
            print(i, j)
