'''
Ao final, seu programa deverá exibir todos os nomes (e respectivo e-mail), um por linha. 

Em cada linha também exibir o próximo (com respectivo e-mail).

'''

import random

nomes = []
emails = []

# ler os nomes e os emails
while True:
    nome = input('Nome: ')
    
    if (nome == ''):
        break

    email = input('e-mail: ')
    
    nomes.append(nome)
    emails.append(email)

# exibir os nomes
print(nomes)
print(emails)


# tamanho do vetor
tamanho = len(nomes)

for i in range(6):
    # gerar duas posições aleatórias
    i1 = random.randint(0, tamanho - 1)
    i2 = random.randint(0, tamanho - 1)

    # permutar os nomes
    aux = nomes[i1]
    nomes[i1] = nomes[i2]
    nomes[i2] = aux

    # permutar os emails
    aux = emails[i1]
    emails[i1] = emails[i2]
    emails[i2] = aux

# Exibir nomes e mails
print(nomes)
print(emails)

# Exibir cada nome com o próximo
for i in range(tamanho):
    prox = i + 1
    if (prox == tamanho):
        prox = 0

    #print(nomes[i], nomes[prox])
    print(f'{nomes[i]}({emails[i]}) -> {nomes[prox]}({emails[prox]})')

