qtd_erros = 0

num = int(input('Número: '))
while (num != 28):
    print('Errou')
    qtd_erros = qtd_erros + 1

    num = int(input('Número: '))

print('acertou')
print(f'Quantidade de erros: {qtd_erros}')
