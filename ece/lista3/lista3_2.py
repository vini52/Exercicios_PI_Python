num_lista = input().split(' ')
num = int(input())
existe = False

for i in range(len(num_lista)):
    for j in range(len(num_lista)):
        if int(num_lista[i]) + int(num_lista[j]) == num and i != j and i < j:
            existe = True
            print('X[{}] + X[{}] = {}'.format(i, j, num))
if existe == False:
    print('NENHUM PAR SOMA {}'.format(num))