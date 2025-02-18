numero = input('Número inteiro: ')

# verificar se é um número inteiro

if (numero.isdigit()):
    numero = int(numero)
    dobro = numero  * 2
    print(numero, dobro)
else:
    print('erro')
