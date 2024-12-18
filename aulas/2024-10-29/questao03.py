media_semestral = int(input('Média semestral: '))
nota_final = int(input('Nota final: '))

# 60% da media semestral + 40% da nota final
media_final = (media_semestral * 0.6) + (nota_final * 0.4)

print(f'Média final = {media_final}')

if media_final >= 50:
    print('Aprovado')
    print('Eita')
    print('Ok')
    print('Parabéns')
    print('Que bom!')
else:
    print('Reprovado')
    print('Sinto muito')
    print('Deveria ter estudado mais')
    print('Chore!')
    print('Receba!!!!')
