a = True
num = int(input())
while num % 2 != 0:
    num = int(input())
lista = []
for i in range(num):
    lista.append(int(input()))

dobra = []
temp = 0
med = int((len(lista) / 2))

for i in range(med):
    temp = lista[i] + lista[(i+1) * -1]
    dobra.append(temp)

print(dobra)