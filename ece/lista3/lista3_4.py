num = int(input())
criancas = []
boas = []
mas = []

for i in range(num):
    criancas.append(input().split(' '))
    if criancas[i][0] == '+':
        boas.append(criancas[i][1:])
    else:
        mas.append(criancas[i][1:])
boas = sorted(boas)
mas = sorted(mas)
mas = mas[::-1]

print('BOAS\n\n====\n')
for i in range(len(boas)):
    print(' '.join(map(str, boas[i])))
    print()
print('\nTotal: {}'.format(len(boas)))

print('\n\n\nMAS\n\n===\n\n')
for i in range(len(mas)):
    print(' '.join(map(str, mas[i])))
    print()
print('\nTotal: {}'.format(len(mas)))
