conjunto_a = input().split(' ')
conjunto_b = input().split(' ')
inter = []
uniao = []
sim = 0

for i in range(len(conjunto_a)):
    if conjunto_a[i] in conjunto_b:
        inter.append(conjunto_a[i])

inter = sorted(inter)
uniao = conjunto_a + conjunto_b
uniao = sorted(uniao)

for i in range(len(uniao)):
    sub = uniao[i+1:]
    for j in range(len(sub)):
        if uniao[i] == sub[j]:
            uniao.remove(sub[j])

sim = (len(inter)) / (len(uniao))

print(f"Interseccao: {' '.join(map(str, inter))}")
print(f"Uniao: {' '.join(map(str, uniao))}")
print(f'Similaridade =  {sim:.2f}')