import random

soma = 0
qtd_20 = 0

# declarar um vetor vazio
numeros = []

# gerar 6 números aleatórios e distintos (1,60)
while True:
    numero = random.randint(1, 60)

    if numero not in numeros:
        numeros.append(numero)

    if len(numeros) == 6:
        break


# exibir todos os números armazenados (um por linha)
for i in range(len(numeros)):
    print(numeros[i])

# somar todos os números armazenados no vetor
soma = sum(numeros)
print('Soma =', soma)

# quantas vezes apareceu o número 20 no vetor
qtd_20 = numeros.count(20)

# qual é o menor e o maior valor que está armazenado no vetor
if (len(numeros) > 0):
    maior = max(numeros)
    menor = min(numeros)
else:
    print('nenhum valor gerado')

# verificar se existe o número 20 armazenado no vetor   
if (20 in numeros):
    indice = numeros.index(20)
    print(f'achei no índice {indice}!')
else:
    print('não achei!')
        
