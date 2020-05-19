def montar_matriz(n:int) -> list:
    m = []
    linha = []
    for i in range(n):
        linha = input().split(' ')
        m.append(linha)
    return m

def add_elementos(m:list, n:int) -> list:
    matriz = []
    for i in range(len(m)):
        const = m[i][len(m[i])-1]
        vetor = m[i]
        for j in range(n):
            vetor.append(const)
        matriz.append(vetor)
    return matriz

def inverter_matriz(v:str) -> float:
    matriz = []
    for i in range(len(v)):
        vet_inv = []
        for j in range(len(v[i]) - 1, -1, -1):
            vet_inv.append(v[i][j])
        matriz.append(vet_inv)
    return matriz

num = input().split(' ')
matriz = inverter_matriz(add_elementos(montar_matriz(int(num[1])), int(num[0])))
matriz = inverter_matriz(add_elementos(matriz, int(num[0])))
aux = 0
for i in matriz:
    string = ''
    for j in i:
        string += j
        string += ' '
    if aux == 0 or aux == int(num[1]) - 1:
        for k in range(int(num[0]) + 1):
            print(string)
            print()
    else:
        print(string)
        print()
    aux += 1
    if int(num[1]) == 1:
        for l in range(int(num[0])):
            print(string)
            print()