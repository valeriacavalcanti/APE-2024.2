import random

# declarar o vetor
numeros = [None] * 100

# preencher o vetor com valores aleatórios
for i in range(100):
    numeros[i] = random.randint(-100,100)

# exibir o vetor
#for i in range(len(numeros)):
#    print(numeros[i])


# Quais são os índices (i) que possuem valores ordenados com seus respectivos sucessores (i+1)
for i in range(0, 99):
    if numeros[i] < numeros[i + 1]:
        print(i)

