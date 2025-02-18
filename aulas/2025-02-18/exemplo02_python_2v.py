"""
    ler e validar um número inteiro
"""

numero = input('Número inteiro: ')
while not numero.isdigit():
    print('tá errado')
    numero = input('Número inteiro: ')

# saiu
numero = int(numero)
dobro = numero  * 2
print(numero, dobro)
