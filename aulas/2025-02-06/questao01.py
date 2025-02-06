# lendo o valor de "n"
n = int(input('N: '))

# declarando os vetores de tamanho "n"
a = [0] * n
b = [0] * n

# ler os "n" valores e armazenar no vetor "a"
for i in range(n):
    a[i] = int(input('Digite o valor: '))
    b[i] = a[i] % 2

# preencher vetor "b"
#for i in range(n):
#    if a[i] % 2 == 1:
 #       b[i] = 1
