"""
 Ler uma frase e exibir a quantidade:
 - símbolo numérico
 - letra maiúscula
 - letra minúscula
 - caracteres especiais
"""
qtd_simbolo_numerico = 0
qtd_letras_maiusculas = 0
qtd_letras_minusculas = 0
qtd_caracteres_especiais = 0

frase = input('Digite uma frase: ')

for i in range(len(frase)):
    #codigo_decimal = ord(frase[i])

    if (frase[i] >= '0') and (frase[i] <= '9'):
        qtd_simbolo_numerico += 1
    else:
        if (frase[i] >= 'A') and (frase[i] <= 'Z'):
            qtd_letras_maiusculas += 1
        else:
            if (frase[i] >= 'a') and (frase[i] <= 'z'):
                qtd_letras_minusculas += 1
            else:
                qtd_caracteres_especiais += 1

print(f'Símbolo Numéricos: {qtd_simbolo_numerico}')
print(f'Letras Maiúsculas: {qtd_letras_maiusculas}')
print(f'Letras Minúsculas: {qtd_letras_minusculas}')
print(f'Caracteres Especiais: {qtd_caracteres_especiais}')
                
