def montar_matriz(n:int) -> list:
    m = []
    linha = []
    for i in range(n):
        linha = input().split(' ')
        m.append(linha)
    return m

def somar_x(m:list) -> int:
    num_linhas = len(m)
    num_colunas = len(m[0])
    soma = 0
    meio = round(((num_linhas-1)/2))
    for i in range(num_linhas):
        for j in range(num_colunas):
            if i == j and i != meio and j != meio:
                soma += int(m[i][j])
    for i in range(num_linhas):
        for j in range(num_colunas-1, -1, -1):
            if i + j == num_linhas - 1:
                soma += int(m[i][j])
    return soma

num = int(input())
matriz = montar_matriz(num)
soma = somar_x(matriz)
print(f'X = {soma}')