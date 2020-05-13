entrada1 = input()
entrada2 = input()

entrada1 = list(entrada1)
entrada2 = list(entrada2)
vetor1 = []
vetor2 = []
i = 0
j = 0

while i < (len(entrada1) - 1):
    if entrada1[i].isdigit() and entrada1[i+1] == ' ':
        vetor1.append(entrada1[i])
    elif entrada1[i].isdigit() and entrada1[i+1].isdigit():
        juntar = entrada1[i] + entrada1[i+1]
        vetor1.append(juntar)
        i += 2 
    i += 1
if entrada1[len(entrada1) - 1].isdigit():
    vetor1.append(entrada1[len(entrada1) - 1])

while j < (len(entrada2) - 1):
    if entrada2[j].isdigit() and entrada2[j+1] == ' ':
        vetor2.append(entrada2[j])
    elif entrada2[j].isdigit() and entrada2[j+1].isdigit():
        juntar1 = entrada2[j] + entrada2[j+1]
        vetor2.append(juntar1)
        j += 2 
    j += 1
if entrada2[len(entrada2) - 1].isdigit():
    vetor2.append(entrada2[len(entrada2) - 1])
    
existe = False


for k in range(len(vetor1)):
    for l in range(len(vetor2)):
        if vetor1[k] == vetor2[l]:
            print(vetor1[k])
            existe = True
            break

if existe == False:
    print('NENHUM ELEMENTO EM COMUM')
        