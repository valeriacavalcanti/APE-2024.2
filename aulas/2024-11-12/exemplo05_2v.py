"""
Ler 6 notas do suap
Exibir: maior e menor nota
"""

nota = int(input(f'1º nota: '))

maior = nota
menor = nota

for i in range(5):
    nota = int(input(f'{i+1}º nota: '))

    if (nota > maior):
        maior = nota
        
    if (nota < menor):
        menor = nota
