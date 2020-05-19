def montar_matriz(n:int) -> list:
    m = []
    linha = []
    for i in range(n):
        linha = input().split(' ')
        m.append(linha)
    return m

def encontrar_maior(m:list) -> int:
    maior = int(m[0][0])
    num_linhas = len(m)
    num_colunas = len(m[0])
    for i in range(num_linhas):
        for j in range(num_colunas):
            if maior < int(m[i][j]):
                maior = int(m[i][j])
    return maior

def apagar_maior(m:list, n:int) -> list:
    num_linhas = len(m)
    num_colunas = len(m[0])
    for i in range(num_linhas):
        for j in range(num_colunas):
            if int(m[i][j]) == n:
                m[i][j] = 0
    return m

num = int(input())
matriz = montar_matriz(num)
maior = encontrar_maior(matriz)
apagar_maior = apagar_maior(matriz, maior)
segundo_maior = encontrar_maior(apagar_maior)
if segundo_maior == 0:
    print('NOT FOUND')
else:
    print(segundo_maior)