def montar_matriz(n:int) -> list:
    m = []
    linha = []
    for i in range(n):
        linha = input().split(' ')
        m.append(linha)
    return m

def superior(m:list) -> list:
    sup = []
    for i in range(len(m)):
        for j in range(len(m[0])):
            if i < j:
                sup.append(m[i][j])
    return sup

def inferior(m:list) -> list:
    inf = []
    for i in range(len(m)):
        for j in range(len(m[0])):
            if i > j:
                inf.append(m[i][j])
    return inf

num = int(input())
matriz = montar_matriz(num)
superior = superior(matriz)
inferior = inferior(matriz)
sup = True
inf = True
for i in superior:
    if float(i) != 0:
        sup = False
for i in inferior:
    if float(i) != 0:
        inf = False
if sup and inf:
    print('diagonal')
elif sup == False and inf:
    print('triangular superior')
elif sup and inf == False:
    print('triangular inferior')
else:
    print('nao triangular')