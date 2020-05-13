t = int(input())
a = int(input())
b = int(input())
tempo_total = 0
alfa = 0
beta = 0
while tempo_total == 0:
    alfa = (t + beta*a) / b
    if alfa - int(alfa) == 0 and t == b * alfa - a * beta:
        tempo_total = alfa * b
    else:
        alfa = (t + beta * b) / a
        if alfa - int(alfa) == 0 and t == a * alfa - b * beta:
            tempo_total = a * alfa
    beta += 1
print(int(tempo_total))