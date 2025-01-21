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
# - Gerar um vetor contendo os números distintos (sem repetição)
# - Exibir vetor gerado

numeros_distintos = []

for i in range(100):
    for j in range(len(numeros_distintos)):
        if (numeros[i] == numeros_distintos[j]):
            break

    if ((len(numeros_distintos) == 0) or (numeros[i] != numeros_distintos[j])):
        numeros_distintos.append(numeros[i])

print(numeros_distintos)
