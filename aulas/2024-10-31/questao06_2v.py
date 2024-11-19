mes = int(input('Informe o mês: '))

if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
    print(f'O mês {mes} tem 31 dias')
elif mes == 2:
    print(f'O mês {mes} tem 29 dias')
else:
    print(f'O mês {mes} tem 30 dias')
