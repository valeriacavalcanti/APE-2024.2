soma_compras = 0
total_cupons = 0
maior_compra = -1
saldo_cupons = 1000
clientes_receberam_todos = 0


for i in range(200):
    valor_compra = float(input('Valor: '))

    qtd_cupons = int(valor_compra // 30)

    soma_compras += valor_compra
    total_cupons += qtd_cupons

    if (qtd_cupons <= saldo_cupons):
        saldo_cupons -= qtd_cupons
        clientes_receberam_todos += 1
    else:
        saldo_cupons = 0

    if (valor_compra > maior_compra):
        maior_compra = valor_compra

    

    
