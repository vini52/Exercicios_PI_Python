num = int(input())
numeros = []
existe = False

for i in range(num):
    numeros.append(int(input()))

for i in range(len(numeros)):
    sub_numeros = numeros[i+1:]
    for j in range(len(sub_numeros)):
        if numeros[i] == sub_numeros[j]:
            existe = True
            dif = len(numeros) - len(sub_numeros)
            indice = dif + j
            print('{}: ({}, {})'.format(numeros[i], i+1, indice+1))
if existe == False:
    print('NAO HA NUMEROS REPETIDOS')