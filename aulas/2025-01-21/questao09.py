import random

# declarar o vetor
numeros = [None] * 100

# preencher o vetor com valores aleatórios
for i in range(100):
    numeros[i] = random.randint(-100,100)

# exibir o vetor
#for i in range(len(numeros)):
#    print(numeros[i])

# A partir dos valores armazenados no vetor "numeros" , exiba:
# - Índices (i) que possuem valores ordenados com seus respectivos
#   sucessores (i+1)

for i in range(99):
    if numeros[i] < numeros[i+1]:
        print(i)
