"""
    ler VÁRIAS palavras!! Até o usuário digitar "fim"
"""
qtd_palavras = 0

palavra = input('Palavras: ')
while palavra.upper() != "FIM":
    qtd_palavras += 1
    palavra = input('Palavras: ')

print(qtd_palavras)
