def preencher_vetor(num) -> list:
    vetor = []
    for i in range(num):
        valores = int(input())
        vetor.append(valores)
    return vetor

def verificar_vizinhos(par:[]):
    for j in range(len(par) - 1):
        a = j + 1
        if par[j] == par[a]:
            b = j
            c = a
            print('Pos {} e {}'.format(b, c))

num = int(input())
par = preencher_vetor(num)
verificar_vizinhos(par)