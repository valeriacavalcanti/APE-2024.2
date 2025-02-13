"""
  ler uma frase e converter para maiúsculo
"""

frase = input('Frase: ')
nova_frase = ''

for i in range(len(frase)):
    if (frase[i] >= 'a') and (frase[i] <= 'z'):
        codigo = ord(frase[i])
        novo_codigo = codigo - 32
        novo_simbolo = chr(novo_codigo)
        nova_frase += novo_simbolo
    else:
        nova_frase += frase[i]

print(frase)
print(nova_frase)

