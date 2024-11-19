import random

qtd_erros = 0
menor, maior = 1, 100

SECRETO = random.randint(menor, maior)

while True:
    num = int(input(f'Número ({menor} e {maior}): '))

    # validando um valor fora do intervalo
    while (num < menor) or (num > maior):
        print('errou o intervalo')
        num = int(input(f'Número ({menor} e {maior}): '))
        
    if (num == SECRETO):
        break
    #print('errou')
    if num > SECRETO:
        print('seu número é maior')
        maior = num - 1
    else:
        print('seu número é menor')
        menor = num + 1
        
    qtd_erros = qtd_erros + 1

    # esgotou tentativas
    if qtd_erros == 4:
        break

    # esgotou chance
    if (menor == maior):
        break

if num == SECRETO:
    print('acertou')
else:
    #print('esgotou chance')
    if qtd_erros == 4:
        print('acabou tentativas')
    else:
        print('não tem mais números')
print(f'Quantidade de erros: {qtd_erros}')
