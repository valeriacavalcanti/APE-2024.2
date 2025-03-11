arq = open('dados.txt', 'r')

lista = arq.read().splitlines()

arq.close()

print(type(lista))
#print(lista)

for i in range(len(lista)):
    print(i, lista[i])

