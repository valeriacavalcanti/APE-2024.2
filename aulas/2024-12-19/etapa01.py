'''
Crie um programa, em Python, para ler e armazenar os nomes de 10 (dez) pessoas.

Exiba todos os nomes armazenados!
'''

nomes = [''] * 10

# ler os nomes
for i in range(10):
    nomes[i] = input('Nome: ')

# exibir os nomes
print(nomes)
