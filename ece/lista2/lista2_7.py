num = int(input())
vetor_v = []
for i in range(num):
    vetor_v.append(int(input()))
if num == 1:
    print(vetor_v)
else:
    for i in range(len(vetor_v) - 1):
        if vetor_v[i] > vetor_v[(i+1) * -1]:
            temp = vetor_v[i]
            temp2 = vetor_v[(i+1) * -1]
            vetor_v[i] = temp2
            vetor_v[(i+1) * -1] = temp
        else:
            break
    print(vetor_v)