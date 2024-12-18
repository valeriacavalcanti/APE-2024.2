import random
soma = 0
qtd_20 = 0
qtd = 0

# declarar um vetor vazio
numeros = []

# gerar vários números (1,30)
while True:
    numero = random.randint(-10, 40)

    if (numero < 1) or (numero > 30):
        break
    
    numeros.append(numero)
    qtd += 1


# exibir todos os números armazenados (um por linha)
for i in range(qtd):
    print(numeros[i])

# somar todos os números armazenados no vetor
for i in range(qtd):
    soma = soma + numeros[i]
print('Soma =', soma)

# quantas vezes apareceu o número 20 no vetor
for i in range(qtd):
    if (numeros[i] == 20):
        qtd_20 = qtd_20 + 1

# qual é o menor e o maior valor que está armazenado no vetor
if (qtd > 0):
    maior = menor = numeros[0]
    for i in range(1,qtd):
        if (numeros[i] > maior):
            maior = numeros[i]
        if (numeros[i] < menor):
            menor = numeros[i]
else:
    print('nenhum valor gerado')

# verificar se existe o número 20 armazenado no vetor
indice = -1
for i in range(qtd):
    if numeros[i] == 20:
        indice = i
        break
    
if (indice != -1):
    print(f'achei no índice {indice}!')
else:
    print('não achei!')
        
