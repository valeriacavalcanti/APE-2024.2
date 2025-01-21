import random

# declarar o vetor
numeros = [None] * 100

# preencher o vetor com valores aleatórios
for i in range(100):
    numeros[i] = random.randint(-100,100)

# exibir o vetor
#for i in range(len(numeros)):
#    print(numeros[i])


# Verificar se tem o número 100 nesse vetor
existe = False
for i in range(100):
    if numeros[i] == 100:
        existe = True
        break

if existe == True:
    print('tem')
else:
    print('nao tem')


# solução Python

if 100 in numeros:
    print('tem')
else:
    print('nao tem')


