vetor = input().split(' ')

convergente = 0

for i in range((len(vetor)//2) - 1):
    if int(vetor[i]) + int(vetor[(i + 1) * -1]) > int(vetor[i+1]) + int(vetor[(i+2) * -1]):
        convergente = True
    else:
        convergente = False
        break

if len(vetor) == 2:
    print('SIM')
elif convergente == True:
    print('SIM')
else:
    print('NAO')