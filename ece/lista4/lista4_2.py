def montar_matriz(n:int) -> list:
    m = []
    linha = []
    for i in range(n):
        linha = input().split(' ')
        m.append(linha)
    return m

def somar_menor(m:list) -> int:
    menores = []
    soma = 0
    for i in range(len(m[0])):
        coluna = []
        for j in range(len(m)):
            coluna.append(int(m[j][i]))
        menores.append(min(coluna))
    soma = sum(menores)
    return soma

num = int(input())
matriz = montar_matriz(num)
soma = somar_menor(matriz)
print(soma)