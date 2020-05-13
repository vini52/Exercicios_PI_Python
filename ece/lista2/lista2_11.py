vetor = []
def encontrar_menor(numeros:list, i:int) -> int:
    indice = 0
    vetor =  []
    vetor = numeros[i:]
    menor = min(vetor)
    for k in range(len(numeros)):
        if vetor[k] == menor:
            dif = 10 - len(vetor)
            indice = dif + k
            return indice

def trocar_posicoes(numeros:list, i:int, j:int) -> list:
    temp = numeros[i]
    numeros[i] = numeros[j]
    numeros[j] = temp
    return numeros

for i in range(10):
    vetor.append(int(input()))

vetor_ordenado = vetor
vetor_final = []
for i in range(int(len(vetor_ordenado) - 1)):
    menor = encontrar_menor(vetor_ordenado, i)
    vetor_final = trocar_posicoes(vetor_ordenado, i, menor)
    if menor != i:
        print('troca {} {}'.format(menor, i))
print(vetor_final)