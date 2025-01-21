import random

# declarar o vetor
numeros = [None] * 100

# preencher o vetor com valores aleatórios
for i in range(100):
    numeros[i] = random.randint(-100,100)

# exibir o vetor
#for i in range(len(numeros)):
#    print(numeros[i])


# Gerar um vetor contendo apenas os números pares que estão armazenados no vetor
pares = []

for i in range(100):
    if numeros[i] % 2 == 0:
        pares.append(numeros[i])

print(pares)

