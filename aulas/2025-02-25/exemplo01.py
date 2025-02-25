# Função para calcular o dobro de um número.
def calcular_dobro(numero):
    dobro = numero * 2
    return dobro

# Função para retornar o nome do IFPB por extenso.
def nome_ifpb():
    return "Instituto Federal de Educação, Ciência e Tecnologia da Paraiba"

# Exibir "n" vezes a palavra "IFPB"
def exibir_ifpb(quantidade = 1):
    for i in range(quantidade):
        print('IFPB')

# Obter a quantidade(n) e exibir "n" vezes a palavra "IFPB"
def exibir_ifpb_2():
    quantidade = int(input('Informe a quantidade de vezes: '))
    for i in range(quantidade):
        print('IFPB')

# Função para exibir todas as letras o alfabeto maiúsculo.
def alfabeto_maiusculo():
    cod_A = ord('A')
    cod_Z = ord('Z')
    for i in range(cod_A, cod_Z + 1):
        print(chr(i))

## programa principal
#num = int(input('Digite um número: '))
#dobro_num = calcular_dobro(num)
#print(num, dobro_num)

#ifpb = nome_ifpb()
#print(ifpb)
#print(nome_ifpb())

exibir_ifpb(2)

#exibir_ifpb_2()
#alfabeto_maiusculo()
