soma_compras = 0
total_cupons = 0
maior_compra = -1
qtd_cupons_maior_compra = 0

for i in range(200):
    valor_compra = float(input('Informe valor da compra: '))
    soma_compras += valor_compra
    
    qtd_cupons = int(valor_compra // 30)
    total_cupons += qtd_cupons

    saldo = valor_compra - (qtd_cupons * 30)
    falta = 30 - saldo

    if (valor_compra > maior_compra):
        maior_compra = valor_compra
        qtd_cupons_maior_compra = qtd_cupons

    if (qtd_cupons > 0):
        print(f'{qtd_cupons} cupons')
    else:
        print('sem cupons')

    print(f'R$ {saldo:.2f} de saldo')
    print(f'R$ {falta:.2f} para novo cupom')

print(f'Total vendido R$ {soma_compras:.2f}')
print(f'Quantidade de cupons distribuídos: {qtd_cupons}')
print(f'Maior valor vendido: R$ {maior_compra:.2f}')
print(f'Quantidade de cupons da maior compra: {qtd_cupons_maior_compra}')