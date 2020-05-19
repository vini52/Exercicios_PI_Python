def montar_matriz(n:int) -> list:
    m = []
    linha = []
    for i in range(n):
        linha = input().split(' ')
        m.append(linha)
    return m
def simetria(m:list) -> bool:
    cont = 0
    for i in range(len(m)):
        for j in range(len(m[0])):
            if m[i][j] != m[j][i]:
                return False
    return True

num = int(input())
matriz = montar_matriz(num)
simetria = simetria(matriz)
if simetria:
    print('S')
else:
    print('N')