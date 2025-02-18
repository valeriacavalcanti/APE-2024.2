"""
    ler uma frase e informar quantas palavras tem nessa frase
"""

frase = input('Digite uma frase: ')
qtd_espacos = 0
qtd_palavras = 0

# contar os espaços
for i in range(len(frase)):
    if frase[i] == ' ':
        qtd_espacos += 1

# calcular quantidade de palavras
if (len(frase) > 0):
    qtd_palavras = qtd_espacos + 1

# exibir
print(qtd_palavras)
