def montar_matriz(n:int) -> list:
    m = []
    linha = []
    for i in range(n):
        linha = input().split(' ')
        m.append(linha)
    return m

def somar_bordas(m:list) -> int:
    num_linhas = len(m)
    num_colunas = len(m[0])
    soma = 0
    for i in range(num_linhas):
        for j in range(num_colunas):
            if i == 0 or i == num_linhas - 1 or j == 0 or j == num_colunas - 1:
                soma += float(m[i][j])
    return soma 

num = input().split(' ')
matriz = montar_matriz(int(num[0]))
bordas = somar_bordas(matriz)
print(f'Borda = {bordas:.2f}')