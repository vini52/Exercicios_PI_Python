n = int(input())
z = 1
for i in range(n,0,-1):
    p = z
    for j in range(p,0,-1):
        print(z,end='')
    print()
    z += 1