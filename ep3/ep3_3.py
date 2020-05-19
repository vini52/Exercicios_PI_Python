num = int(input())
pi = 0
for i in range(num):
    pi += (-1)**i/(2*i+1)
print(f'{pi*4:.3f}')