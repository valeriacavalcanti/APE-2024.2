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
# - Gerar um vetor contendo apenas os números pares que estão
#   armazenados no vetor
# - Exibir vetor gerado

numeros_pares = []

for i in range(100):
    if numeros[i] % 2 == 0:
        numeros_pares.append(numeros[i])

print(numeros_pares)
