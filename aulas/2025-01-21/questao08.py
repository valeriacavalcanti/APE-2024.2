import random

# declarar o vetor
numeros = [None] * 100

# preencher o vetor com valores aleatórios
for i in range(100):
    numeros[i] = random.randint(-100,100)

# exibir o vetor
#for i in range(len(numeros)):
#    print(numeros[i])


# Verificar se uma posição aleatória (p) e seu sucessor (p + 1) possuem valores ordenados

p = random.randint(0,99)

if numeros[p] < numeros[p + 1]:
    print('ordenados', numeros[p], numeros[p + 1])
elif numeros[p] > numeros[p + 1]:
    print('nao ordenados', numeros[p], numeros[p + 1])
else:
    print('constantes (iguais)')

