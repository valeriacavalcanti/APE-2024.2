import funcoes

# main
num1 = int(input('Primeiro número: '))
num2 = int(input('Segundo número: '))

soma_numeros = funcoes.somar(num1, num2)
print(soma_numeros)
print(funcoes.somar(10,10))     # 20
print(funcoes.somar(10,-10))    # 0
print(funcoes.somar(-10,-10))   # -20
print(funcoes.somar(2.5, 3.2))  # 5.7
print(funcoes.multiplicar(10,8))# 80
