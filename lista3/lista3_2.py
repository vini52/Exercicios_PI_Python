l = int(input())
c = l
x = 'o'
y = '*'
z = 0
for i in range(l):
    if c == 0:
        print()
        if z % 2 == 0:
            x = '*'
            y = 'o'
        z += 1
        c = l
    else:
        print(x, end='')
        c -= 1
        print(y, end='')
        c -= 1