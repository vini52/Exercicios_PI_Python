def montar_matriz(n:int) -> list:
    m = []
    linha = []
    for i in range(n):
        linha = input().split(' ')
        m.append(linha)
    return m

num = input().split(' ')
matriz = montar_matriz(int(num[0]))
vetor = input().split(' ')
if len(matriz[0]) != len(vetor):
    print('nao eh possivel fazer a operacao')
else:
    y = []
    for linha in matriz:
        soma = 0
        for i in range(len(vetor)):
            soma += float(vetor[i]) * float(linha[i])
        y.append(soma)
    for elemento in y:
        print(f'{elemento:.1f}')