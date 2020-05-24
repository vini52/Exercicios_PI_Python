def montar_matriz(n:int) -> list:
    m = []
    linha = []
    for i in range(n):
        linha = input().split(' ')
        m.append(linha)
    return m

def dobrar_matriz(m:list) -> list:
    matriz_dobrada = []
    if len(m[0]) % 2 != 0:
        print('numero impar de colunas')
    else:
        for linha in m:
            soma = 0
            dobra = []
            for i in range(len(linha)//2):
                soma = int(linha[i]) + int(linha[(i+1) * -1])
                dobra.append(soma)
            matriz_dobrada.append(dobra)
    return matriz_dobrada

num = int(input())
matriz = montar_matriz(num)
dobra = dobrar_matriz(matriz)

for linha in dobra:
    for num in linha:
        print(f'{num:.1f}', end=' ')
    print()