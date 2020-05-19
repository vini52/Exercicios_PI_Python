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

def diagonal(m:list) -> list:
    diag = []
    for i in range(len(m)):
        for j in range(len(m[0])):
            if i == j:
                diag.append(m[i][j])
    return diag

num = int(input())
matriz = montar_matriz(num)
superior = superior(matriz)
inferior = inferior(matriz)
diagonal = diagonal(matriz)
soma_sup = 0
soma_inf = 0
soma_diag = 0
for i in superior:
    soma_sup += float(i)
for i in inferior:
    soma_inf += float(i)
for i in diagonal:
    soma_diag += float(i)
res = (soma_sup + soma_inf) - soma_diag
print(f'Resultado = {res:.2f}')