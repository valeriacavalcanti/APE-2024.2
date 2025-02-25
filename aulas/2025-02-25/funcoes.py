# Função para somar dois número inteiros.
def somar(valor1: int, valor2: int) -> int:
    soma = 0
    if valor1 > 0:
        soma += valor1
    if valor2 > 0:
        soma += valor2
    return soma


# Função para multiplicar dois número inteiros.
def multiplicar(valor1: int, valor2: int) -> int:
    return valor1 * valor2
