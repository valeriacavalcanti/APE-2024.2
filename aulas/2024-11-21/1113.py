x, y = input().split()
x, y = int(x), int(y)

while (x != y):
    if (x > y):
        print('Decrescente')
    else:
        print('Crescente')
    x, y = input().split()
    x, y = int(x), int(y)
