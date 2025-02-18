while True:
    numero = input('Número inteiro: ')

    # verificar se é um número inteiro
    e_numero = True

    for i in range(len(numero)):
        if (numero[i] < '0') or (numero[i] > '9'):
            e_numero = False
            break

    if (e_numero):
        break

    print('tá errado')


# saiu
numero = int(numero)
dobro = numero  * 2
print(numero, dobro)
