entrada = input().split(' ')
vetor = entrada
temp = 0
i = 0
while i < len(entrada):
    if entrada[i].isdigit():
        vetor.append(entrada[i])
        i += 1
    else:
        if entrada[i] == '+':
            temp = int(entrada[i-2]) + int(entrada[i-1])
            vetor.append(temp)
            print(vetor)
            vetor.remove(entrada[i-1])
            vetor.remove(entrada[i-2])
            print(vetor)
            i += 1
        elif entrada[i] == '-':
            temp = int(entrada[i-2]) - int(entrada[i-1])
            vetor.append(temp)
            vetor.remove(entrada[i-1])
            vetor.remove(entrada[i-2])
            i += 1
        elif entrada[i] == '*':
            temp = int(entrada[i-2]) * int(entrada[i-1])
            vetor.append(temp)
            print(vetor)
            vetor.remove(entrada[i-1])
            vetor.remove(entrada[i-2])
            print(vetor)
            i += 1
        elif entrada[i] == '/':
            temp = int(entrada[i-2]) / int(entrada[i-1])
            vetor.append(temp)
            vetor.remove(entrada[i-1])
            vetor.remove(entrada[i-2])
            i += 1
        i += 1
print(vetor)