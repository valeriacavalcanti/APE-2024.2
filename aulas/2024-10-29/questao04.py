import math

tempo_avaliacao = int(input('Tempo da avaliação: '))

qtd_aulas = tempo_avaliacao / 3000
qtd_aulas = math.ceil(qtd_aulas)

# misterio = round(qtd_aulas, 0)

print(f'Quantidade de aulas: {qtd_aulas}')
