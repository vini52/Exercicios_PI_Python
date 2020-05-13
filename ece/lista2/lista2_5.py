import math

pontos1 = input()
pontos2 = input()
e1 = pontos1.count(' ')
e2 = pontos2.count(' ')
pontos1 += ' '
pontos2 += ' '
temp = ''
pontos_list1 = []
pontos_list2 = []

if e1 != e2:
    print('ERRO')
else:
    for char in pontos1:
        if char == ' ':
            pontos_list1.append(temp)
            temp = ''
        else:
            temp += char
    for char in pontos2:
        if char == ' ':
            pontos_list2.append(temp)
            temp = ''
        else:
            temp += char
    distancia = 0
    for i in range(len(pontos_list1)):
        p1 = float(pontos_list1[i])
        p2 = float(pontos_list2[i])
        distancia += (math.pow((p1 - p2), 2))
    distancia = math.sqrt(distancia)
    print('{:.2f}'.format(distancia))
    