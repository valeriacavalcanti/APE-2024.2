arq = open('dados.txt', 'r')

textao = arq.read()

arq.close()

print(type(textao))
print(textao)
