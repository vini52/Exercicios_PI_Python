n = int(input())
res1 = 0
res2 = 1
for i in range(n):
    res2 += res1
    res1 -= res2
print(res2)
    # if res == n:
    #     print('Verdadeiro')
    #     break
