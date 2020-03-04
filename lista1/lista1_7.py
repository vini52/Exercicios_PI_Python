saque = int(input())
ced100 = 0
ced50 = 0
ced20 = 0
ced10 = 0
ced5 = 0
ced2 = 0
ced1 = 0
while saque > 0:
    if saque >= 100:
        ced100 += 1
        saque -= 100
    elif saque >= 50 and saque < 100:
        ced50 += 1
        saque -= 50
    elif saque >= 20 and saque < 50:
        ced20 += 1
        saque -= 20
    elif saque >= 10 and saque < 20:
        ced10 += 1
        saque -= 10
    elif saque >= 5 and saque < 10:
        ced5 += 1
        saque -= 5
    elif saque >= 2 and saque < 5:
        ced2 += 1
        saque -= 2
    else:
        ced1 += 1
        saque -= 1
print("{} nota(s) de R$ 100\n{} nota(s) de R$ 50\n{} nota(s) de R$ 20\n{} nota(s) de R$ 10\n{} nota(s) de R$ 5\n{} nota(s) de R$ 2\n{} nota(s) de R$ 1".format(ced100,ced50,ced20,ced10,ced5,ced2,ced1))