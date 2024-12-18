valor_compra = float(input('Valor da compra: '))

if valor_compra > 100:
    valor_desconto = valor_compra * 0.1
    valor_compra = valor_compra - valor_desconto

print(f'Valor compra: R$ {valor_compra:.2f}')
print('Valor compra: R$ {:.2f}'.format(valor_compra))
