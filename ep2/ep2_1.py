nota1 = float(input())
nota2 = float(input())
media1 = (nota1 + nota2) / 2
if media1 >= 5:
    print('{:.2f}'.format(media1))
    print('APROVADO')
else:
    recuperacao = float(input())
    media2 = (media1 + recuperacao) / 2
    if media2 >= 5:
        print('{:.2f}'.format(media1))
        print('{:.2f}'.format(media2))
        print('APROVADO')
    else:
        print('{:.2f}'.format(media1))
        print('{:.2f}'.format(media2))
        print('REPROVADO')