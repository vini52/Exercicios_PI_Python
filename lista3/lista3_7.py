n = int(input())
x = 0
y = 0
j = 0
for i in range(n):
    num = int(input())
    if j != 1:
        if num < x:
            y = i + 1
            j = 1
    x = num
print(y)