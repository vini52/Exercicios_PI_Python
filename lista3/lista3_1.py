l = int(input())
c = int(input())
if l == 1 and c == 1:
    print('*' * c)
elif l > 0 and c == 1:
    for i in range(l):
        print('*')
elif l == 1:
    print('*' * c)
else:
    print('*' * c)
    for i in range(l-2):
        print('*' + ' ' * (c-2) + '*')
    print('*' * c)