"""
   Exibir símbolos numéricos, alfabeto maiúsculo, minúsculo
"""

# símbolos numéricos
cod_0 = ord('0')
cod_9 = ord('9')

print('símbolos numéricos')
for i in range(cod_0, cod_9 + 1):
    print(i, chr(i), bin(i), hex(i), oct(i))


# ALFABETO MAIÚSCULO
cod_A = ord('A')
cod_Z = ord('Z')

print('\nALFABETO MAIÚSCULO')
for i in range(cod_A, cod_Z + 1):
    print(i, chr(i), bin(i), hex(i), oct(i))


# alfabeto minúsculo
cod_a = ord('a')
cod_z = ord('z')

print('\nalfabeto minúsculo')
for i in range(cod_a, cod_z + 1):
    print(i, chr(i), bin(i), hex(i), oct(i))
