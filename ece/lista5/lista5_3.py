def montar_matriz(n:int) -> list:
    m = []
    linha = []
    for i in range(n):
        linha = input().split(' ')
        m.append(linha)
    return m

def verificar_daora(m:list) -> bool:
    a1 = []
    a2 = []
    b1 = []
    b2 = []
    cont = 0
    for i in range(len(m)):
        for j in range(len(m[0])):
            if i == j and i < (len(m) // 2):
                a1.append(m[i][j])
            elif i == j and i > (len(m) // 2):
                a2.append(m[i][j])
    for i in range(len(m)):
        for j in range(len(m) - 1, -1, -1):
            if i + j == len(m[0]) - 1:
                if i < (len(m) // 2):
                    b1.append(m[i][j])
                elif i > (len(m) // 2):
                    b2.append(m[i][j])
    a2.reverse()
    b2.reverse()
    for i in range(len(a1)):
        if (int(a1[i]) + int(a2[i])) >= (int(b1[i]) + int(b2[i])):
            cont += 1
    if cont == len(a1):
        return True
    else:
        return False

num = input().split(' ')
matriz = montar_matriz(int(num[0]))

if num[0] != num[1]:
    print('NAO EH DAORA')
else:
    if verificar_daora(matriz):
        print('EH DAORA')
    else:
        print('NAO EH DAORA')