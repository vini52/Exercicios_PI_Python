def verificar_movimentos(x:int, y:int) -> list:
    mov_x = []
    mov_y = []
    movimentos = []

    if y >= 2 and x <= 6:
        mov_y.append(y - 2)
        mov_x.append(x + 1)
    if y >= 2 and x >= 1:
        mov_y.append(y - 2)
        mov_x.append(x - 1)
    if y <= 5 and x >= 1:
        mov_y.append(y + 2)
        mov_x.append(x - 1)
    if y <= 5 and x <= 6:
        mov_y.append(y + 2)
        mov_x.append(x + 1)
    if y >= 1 and x >= 2:
        mov_y.append(y - 1)
        mov_x.append(x - 2)
    if y <= 6 and x >= 2:
        mov_y.append(y + 1)
        mov_x.append(x - 2)
    if y >= 1 and x <= 5:
        mov_y.append(y - 1)
        mov_x.append(x + 2)
    if y <= 6 and x <= 5:
        mov_y.append(y + 1)
        mov_x.append(x + 2)

    for i in range(len(mov_y)):
        movimentos.append(str(mov_x[i]) + ' ' + str(mov_y[i]))

    movimentos.sort()

    return movimentos  

posicao = input().split(' ')
movimentos = verificar_movimentos(int(posicao[0]), int(posicao[1]))
for pos in movimentos:
    print(pos)