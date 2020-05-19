def montar_matriz(n:int) -> list:
    m = []
    linha = []
    for i in range(n):
        linha = input().split(' ')
        m.append(linha)
    return m

def procurar_42(m:list) -> list:
    posicao = []
    for i in range(len(m)):
        for j in range(len(m[0])):
            if i != 0 or i != len(m) - 1 or j != 0 or j != len(m[0]) - 1:
                if int(m[i][j]) == 42 and int(m[i][j-1]) == 7 and int(m[i-1][j]) == 7 and int(m[i-1][j-1]) == 7 and int(m[i+1][j+1]) == 7 and int(m[i+1][j-1]) == 7 and int(m[i-1][j+1]) == 7 and int(m[i+1][j]) == 7 and int(m[i][j+1]) == 7:
                    posicao.append(i+1)
                    posicao.append(j+1)
    return posicao

num = input().split(' ')
matriz = montar_matriz(int(num[0]))
posicao = procurar_42(matriz)
if posicao:
    for pos in posicao:
        print(pos, end=' ')
else:
    print('0 0')