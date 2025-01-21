'''
Altere o programa para sortear aleatoriamente duas posições e permutar os nomes entre elas.

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

# permutar duas posições aleatórias
tamanho = len(nomes)
i1 = random.randint(0, tamanho - 1)
i2 = random.randint(0, tamanho - 1)

aux = nomes[i1]
nomes[i1] = nomes[i2]
nomes[i2] = aux

# exibir todos os nomes
print(nomes)
