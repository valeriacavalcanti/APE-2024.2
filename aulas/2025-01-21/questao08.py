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
# - Se uma posição aleatória (p) e seu sucessor (p + 1) possuem
#   valores ordenados (crescente)

p = random.randint(0,98)

if numeros[p] < numeros[p+1]:
    print('ordenado')
else:
    print('nao ordenado')
