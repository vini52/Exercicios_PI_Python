def montar_matriz(n:int) -> list:
    m = []
    linha = []
    for i in range(n):
        linha = input().split(' ')
        m.append(linha)
    return m

def somar_taca(m:list) -> float:
    soma = 0
    for num in m[0]:
        soma += float(num)
    for i in range(1, int((len(m)/2) + 0.5)):
        linha = m[i][i:-i]
        for num in linha:
            soma += float(num)
    return soma

num = int(input())
matriz = montar_matriz(num)
soma_taca = somar_taca(matriz)
print(f'Resultado = {soma_taca:.2f}')