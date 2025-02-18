"""
    ler uma data
"""

dia, mes, ano = input("Digite uma data: ").split('/')
dia, mes, ano = int(dia), int(mes), int(ano)

print(dia, type(dia))
print(mes, type(mes))
print(ano, type(ano))
