valor_compra = float(input('Valor da compra: '))

if valor_compra <= 100:
    cashback = valor_compra * 0.04
elif valor_compra <= 200:
    cashback = valor_compra * 0.06
elif valor_compra <= 400:
    cashback = valor_compra * 0.08
else:
    cashback = valor_compra * 0.1

print(f'Cashback = {cashback}')
