'''
Altere o programa para 6 vezes sortear aleatoriamente duas posições e permutar os nomes entre elas.

Exiba todos os nomes armazenados!

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

# exibir todos os nomes
print(nomes)
