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
# - Se tem o número 100 nesse vetor

for i in range(100):
    if numeros[i] == 100:
        break

if numeros[i] == 100:
    print('tem, na posicao', i)
else:
    print('nao tem')


print(100 in numeros)
