'''
Altere o programa para permutar o primeiro nome com o último nome armazenado.

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

# permutar a primeira com a última posição
primeiro = 0
ultimo = len(nomes) - 1

aux = nomes[primeiro]
nomes[primeiro] = nomes[ultimo]
nomes[ultimo] = aux

# exibir todos os nomes
print(nomes)
