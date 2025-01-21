import random

# declarar o vetor
numeros = [None] * 100

# preencher o vetor com valores aleatórios
for i in range(100):
    numeros[i] = random.randint(-100,100)

#numeros = list(range(100))

# exibir o vetor
#for i in range(len(numeros)):
#    print(numeros[i])


# A partir dos valores armazenados no vetor "numeros" , exiba:
# - Se o vetor está ordenado ou não

ordenado = True

for i in range(99):
    if numeros[i] > numeros[i + 1]:
        ordenado = False
        break

if ordenado == True:
    print('ordenada')
else:
    print('nao ordenada')




