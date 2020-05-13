n = int(input())
for i in range(1, 4 * n + 1):
    if i % 4 == 0:
        print('PIM\n')
    else:
        print(i, end = ' ')