def montar_matriz(n:int) -> list:
    m = []
    linha = []
    for i in range(n):
        linha = input().split(' ')
        m.append(linha)
    return m

def somar_torre(m:list) -> int:
    colunas = []
    maior = 0
    soma = 0
    for i in range(len(m)):
        coluna = []
        for j in range(len(m)):
            for num in m[i]:
                m[i][j] = int(m[i][j])
            coluna.append(int(m[j][i]))
        colunas.append(coluna)
    for i in range(len(m)):
        for j in range(len(m)):
            soma = sum(m[i]) + sum(colunas[j]) - (2 * m[i][j])
            if soma > maior:
                maior = soma
    return maior

num = int(input())
matriz = montar_matriz(num)
soma = somar_torre(matriz)
print(soma)