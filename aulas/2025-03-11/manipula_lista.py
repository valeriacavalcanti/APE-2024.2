# Gerar uma lista de tamanho n com valores aleatórios.
def gerar_lista(quantidade: int, menor_valor: int, maior_valor: int) -> list:
    import random
    lista = [0] * quantidade
    for i in range(quantidade):
        lista[i] = random.randint(menor_valor, maior_valor)
    return lista

# Exibir os elementos da lista, um por linha.
def exibir_lista(lista: list):
    for i in range(len(lista)):
        print(lista[i])

# Calcular a média dos valores da lista.
def calcular_media(lista: list) -> float:
    soma = 0
    for i in range(len(lista)):
        soma += lista[i]
    return soma/len(lista)

# Elementos com valores acima da média.
def elementos_acima_da_media(lista: list) -> list:
    media = calcular_media(lista)
    elementos = []
    for i in range(len(lista)):
        if lista[i] > media:
            elementos.append(lista[i])
    return elementos

# Elementos com valores abaixo da média.
def elementos_abaixo_da_media(lista: list) -> list:
    media = calcular_media(lista)
    elementos = []
    for i in range(len(lista)):
        if lista[i] < media:
            elementos.append(lista[i])
    return elementos

# Elementos com valores entre (inclusive) dois valores informados.
def elementos_entre_dois_valores(lista: list, valor1: int, valor2: int) -> list:
    elementos = []
    for i in range(len(lista)):
        if ((lista[i] >= valor1) and (lista[i] <= valor2)):
            elementos.append(lista[i])
    return elementos

# Elementos com valores fora de um intervalo informado.
def elementos_fora_de_um_intervalo(lista: list, valor1: int, valor2: int) -> list:
    elementos = []
    for i in range(len(lista)):
        if ((lista[i] < valor1) or (lista[i] > valor2)):
            elementos.append(lista[i])
    return elementos

# Elementos distintos da lista.
def elementos_distintos(lista: list) -> list:
    memoria = []
    for i in range(len(lista)):
        if lista[i] not in memoria:
            memoria.append(lista[i])
    return memoria

# Elemento mais frequente. Pode haver repetição.
def elemento_mais_frequente(lista: list) -> list:
    distintos = elementos_distintos(lista)
    frequencia = [0] * len(distintos)

    for i in range(len(distintos)):
        frequencia[i] = lista.count(distintos[i])

    maior = max(frequencia)
    mais_frequente = []

    for i in range(len(frequencia)):
        if frequencia[i] == maior:
            mais_frequente.append(distintos[i])

    return mais_frequente

# Calcular a quantidade de elementos com valores acima da média.
def quantidade_elementos_acima_da_media(lista: list) -> int:
    elementos = elementos_acima_da_media(lista)
    return len(elementos)

# Calcular a quantidade de elementos com valores abaixo da média.
def quantidade_elementos_abaixo_da_media(lista: list) -> int:
    return len(elementos_abaixo_da_media(lista))

# Calcular a quantidade de elementos com valores entre (inclusive) dois valores informados.
def quantidade_elementos_entre_dois_valores(lista: list, menor_valor: int, maior_valor: int) -> int:
    return len(elementos_entre_dois_valores(lista, menor_valor, maior_valor))

# Calcular a quantidade de elementos com valores fora de um intervalo informado.
def quantidade_elementos_fora_de_um_intervalo(lista: list, menor_valor: int, maior_valor: int) -> int:
    return len(elementos_fora_de_um_intervalo(lista, menor_valor, maior_valor))

# Calcular a quantidade de elementos distintos da lista
def quantidade_elementos_distintos(lista: list) -> int:
    return len(elementos_distintos(lista))
