import random

# declarar o vetor
numeros = [None] * 100

# preencher o vetor com valores aleatórios
for i in range(100):
    numeros[i] = random.randint(-100,100)

# exibir o vetor
#for i in range(len(numeros)):
#    print(numeros[i])


# Verificar se o vetor está ordenado
vetor_ordenado = True

for i in range(99):
    if numeros[i] > numeros[i + 1]:
        vetor_ordenado = False
        break

if vetor_ordenado == True:
    print('vetor ordenado')
else:
    print('vetor não ordenado')
