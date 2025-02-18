"""
    ler uma frase e informar quantas palavras tem nessa frase
"""

frase = input('Digite uma frase: ')
qtd_espacos = 0
qtd_palavras = 0

# contar os espaços
qtd_espacos = frase.count(' ')

# calcular quantidade de palavras
if (len(frase) > 0):
    qtd_palavras = qtd_espacos + 1

# exibir
print(qtd_palavras)
