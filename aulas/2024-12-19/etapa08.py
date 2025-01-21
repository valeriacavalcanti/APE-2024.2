'''
Altere o programa para não sortear e sim 
exibir todos os nomes, um por linha.

Em cada linha também exibir o próximo!

'''

import random

nomes = []

# ler os nomes
while True:
    nome = input('Nome: ')
    
    if (nome == ''):
        break

    nomes.append(nome)

# exibir os nomes
print(nomes)

# tamanho do vetor
tamanho = len(nomes)

for i in range(6):
    # permutar duas posições aleatórias
    i1 = random.randint(0, tamanho - 1)
    i2 = random.randint(0, tamanho - 1)

    aux = nomes[i1]
    nomes[i1] = nomes[i2]
    nomes[i2] = aux

# Exibir nomes
print(nomes)

# Exibir cada nome com o próximo
for i in range(tamanho):
    prox = i + 1
    if (prox == tamanho):
        prox = 0

    print(nomes[i], nomes[prox])



