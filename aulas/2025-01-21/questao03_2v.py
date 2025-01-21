import random

# declarar o vetor
numeros = [None] * 100

# preencher o vetor com valores aleatórios
for i in range(100):
    numeros[i] = random.randint(-100,100)

# exibir o vetor
#for i in range(len(numeros)):
#    print(numeros[i])


# Menor e maior valores armazenados
maior = menor = numeros[0]

for i in range(1,100):
    if numeros[i] < menor:
        menor = numeros[i]
    if numeros[i] > maior:
        maior = numeros[i]

print(menor, maior)

