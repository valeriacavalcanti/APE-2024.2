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
# - Menor e maior valores armazenados

maior = -101
menor = 101

for i in range(100):
    if numeros[i] < menor:
        menor = numeros[i]
    if numeros[i] > maior:
        maior = numeros[i]

print(menor, maior)
