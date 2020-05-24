def montar_matriz(n:int) -> list:
    m = []
    linha = []
    for i in range(n):
        linha = input().split(' ')
        m.append(linha)
    return m

def encontrar_menor(m:list) -> int:
    menor = int(m[0][0])
    for num in m[0]:
        if int(num) < menor:
            menor = int(num)
    for num in m[-1]:
        if int(num) < menor:
            menor = int(num)
    for i in range(len(m)):
        for j in range(len(m[0]) - 2, 0, -1):
            if i + j == len(m[0]) - 1:
                if menor > int(m[i][j]):
                    menor = int(m[i][j])
    return menor

num = int(input())
matriz = montar_matriz(num)
menor = encontrar_menor(matriz)
print(menor)