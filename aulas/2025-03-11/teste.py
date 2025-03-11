import manipula_lista as ml

# Função: gerar_lista
# Objetivo: Gerar uma lista com valores aleatórios.
# Parâmetros: quantidade (int), menor_valor (int), maior_valor (int)
# Retorno: números gerados em um list.
numeros = ml.gerar_lista(4, 1, 5)
print(numeros)

# Função: exibir_lista
# Exibir os elementos da lista.
# Parâmetros: lista (list)
# Retorno: -- sem retorno --
ml.exibir_lista(numeros)

# Função: calcular_media
# Objetivo: Calcular a média dos valores da lista.
# Parâmetros: lista (list)
# Retorno: média (float)
media = ml.calcular_media(numeros)
print(f'Média: {media:.2f} ({type(media)})')

# Função: elementos_acima_da_media
# Objetivo: Elementos com valores acima da média.
# Parâmetros: lista (list)
# Retorno: lista com valores acima da média (list)
acima_media = ml.elementos_acima_da_media(numeros)
print(f'Acima da média: {acima_media} ({type(acima_media)})')

# Função: elementos_abaixo_da_media
# Objetivo: Elementos com valores abaixo da média.
# Parâmetros: lista (list)
# Retorno: lista com valores abaixo da média (list)
abaixo_media = ml.elementos_abaixo_da_media(numeros)
print(f'Abaixo da média: {abaixo_media} ({type(abaixo_media)})')

# Função: elementos_entre_dois_valores
# Objetivo: Elementos com valores entre (inclusive) dois valores informados.
# Parâmetros: lista (list), valor1 (menor) e valor2 (maior)
# Retorno: lista com valores entre menor e maior (list)
entre_valores = ml.elementos_entre_dois_valores(numeros, 1, 50)
print(f'Entre valores: {entre_valores} ({type(entre_valores)})')

# Função: elementos_fora_de_um_intervalo
# Objetivo: Elementos com valores fora do intervalo.
# Parâmetros: lista (list), valor1 (menor) e valor2 (maior)
# Retorno: lista com valores fora do intervalo (list)
fora_intervalo = ml.elementos_fora_de_um_intervalo(numeros, 10, 90)
print(f'Fora do intervalo: {fora_intervalo} ({type(fora_intervalo)})')

# Função: elementos_distintos
# Objetivo: Elementos distintos da lista.
# Parâmetros: lista (list)
# Retorno: lista com elementos sem repetição (list)
distintos = ml.elementos_distintos(numeros)
print(f'Elementos distintos: {distintos} ({type(distintos)})')


# Função: quantidade_elementos_acima_da_media
# Objetivo: Calcular a quantidade de elementos com valores acima da média.
# Parâmetros: lista (list)
# Retorno: quantidade de elementos acima da média (int)
quantidade_acima_media = ml.quantidade_elementos_acima_da_media(numeros)
print(f'Quantidade acima da média: {quantidade_acima_media} ({type(quantidade_acima_media)})')

# Função: quantidade_elementos_abaixo_da_media
# Objetivo: Calcular a quantidade de elementos com valores abaixo da média.
# Parâmetros: lista (list)
# Retorno: quantidade de elementos abaixo da média (int)
quantidade_abaixo_media = ml.quantidade_elementos_abaixo_da_media(numeros)
print(f'Quantidade abaixo da média: {quantidade_abaixo_media} ({type(quantidade_abaixo_media)})')


# Função: elemento_mais_frequente
# Objetivo: Elemento mais frequente. Pode haver repetição.
# Parâmetros: lista (list)
# Retorno: lista com valores mais frequentes (list)
mais_frequente = ml.elemento_mais_frequente(numeros)
print(f'Mais frequente: {mais_frequente} ({type(mais_frequente)})')

