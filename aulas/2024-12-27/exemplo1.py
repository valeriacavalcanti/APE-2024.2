import random
soma = 0
qtd_20 = 0

# declarar um vetor de tamanho 6
numeros = [0] * 6

# gerar 6 valores aleatórios (1 - 60)
for i in range(6):
    numeros[i] = random.randint(1, 30)
    #print(numeros)

# exibir todos os números armazenados (um por linha)
for i in range(6):
    print(numeros[i])

# somar todos os números armazenados no vetor
for i in range(6):
    soma = soma + numeros[i]
print('Soma =', soma)

# quantas vezes apareceu o número 20 no vetor
for i in range(6):
    if (numeros[i] == 20):
        qtd_20 = qtd_20 + 1

# qual é o menor e o maior valor que está armazenado no vetor
maior = menor = numeros[0]
for i in range(6):
    if (numeros[i] > maior):
        maior = numeros[i]
    if (numeros[i] < menor):
        menor = numeros[i]

# verificar se existe o número 20 armazenado no vetor
indice = -1
for i in range(6):
    if numeros[i] == 20:
        indice = i
        break
    
if (indice != -1):
    print(f'achei no índice {indice}!')
else:
    print('não achei!')
        
