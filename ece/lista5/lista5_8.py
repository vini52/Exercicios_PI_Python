def montar_matriz(n:int) -> list:
    m = []
    linha = []
    for i in range(n):
        linha = input().split(' ')
        m.append(linha)
    return m

def somar_diagonal(m:list) -> list:
    matriz = m
    for i in range(len(m)):
        for j in range(len(m)):
            if i != j:
                matriz[j][i] = int(matriz[j][i]) + int(matriz[i][j])
    return matriz

def dobrar_diagonal(m:list) -> list:
    for i in range(len(m)):
        for j in range(len(m)):
            if i + j <= i * 2:
                print(m[i][j], end=' ')
        print()

num = int(input())
matriz = montar_matriz(num)
soma_matriz = somar_diagonal(matriz)
dobra = dobrar_diagonal(soma_matriz)