import random

# declarar o vetor
numeros = [None] * 100

# preencher o vetor com valores aleatórios
for i in range(100):
    numeros[i] = random.randint(-100,100)

# exibir o vetor
#for i in range(len(numeros)):
#    print(numeros[i])


# Gerar um vetor contendo os números distintos (sem repetição)
distintos = []

for i in range(100):
    if numeros[i] not in distintos:
        distintos.append(numeros[i])

print(distintos)

