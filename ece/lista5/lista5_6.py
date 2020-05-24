def montar_matriz(n:int) -> list:
    m = []
    linha = []
    for i in range(n):
        linha = input().split(' ')
        m.append(linha)
    return m

def verificar_linhas(m:list) -> bool:
    for linha in m:
        if linha.count('1') > 1 or linha.count('0') < (len(linha) - 1):
            return False
    return True

def verificar_colunas(m:list) -> bool:
    colunas = []
    for i in range(len(m)):
        coluna = []
        for j in range(len(m)):
            coluna.append(m[j][i])
        colunas.append(coluna)
    for coluna in colunas:
        if coluna.count('1') > 1 or coluna.count('0') < (len(coluna) - 1):
            return False
    return True

num = int(input())
matriz = montar_matriz(num)
linhas = verificar_linhas(matriz)
colunas = verificar_colunas(matriz)
if num == 1:
    print('NAO')
elif linhas and colunas:
    print('SIM')
else:
    print('NAO')