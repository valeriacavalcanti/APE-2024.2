"""
Para ler 10 números, calcular e exibir
a média dos números pares.
"""
soma_pares = 0
qtd_pares = 0

for i in range(4):
    num = int(input('Número: '))
    if (num % 2 == 0):
        soma_pares = soma_pares + num
        qtd_pares = qtd_pares + 1
        # soma_pares += num
        # qtd_pares += 1

if qtd_pares > 0:
    media_pares = soma_pares / qtd_pares
    print(f'Média = {media_pares}')
else:
    print('Erro: nenhum número foi par')
