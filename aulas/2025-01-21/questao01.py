import random

# declarar o vetor
numeros = [None] * 100

# preencher o vetor com valores aleatórios
for i in range(100):
    numeros[i] = random.randint(-100,100)

# exibir o vetor
#for i in range(len(numeros)):
#    print(numeros[i])


# Somar os números negativos
soma = 0
for i in range(100):
    if numeros[i] < 0:
        soma += numeros[i]

print(soma)
