"""
    ler uma frase e limpar os espaços em branco em excesso
"""

frase = input('Digite uma frase: ')

while frase.count('  ') > 0:
    frase = frase.replace('  ', ' ')

frase = frase.strip()

print(frase)
