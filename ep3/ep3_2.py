num = int(input())
div = 0
for i in range(1, num+1):
    if num % i == 0:
        div += 1
if div == 2:
    print('SIM')
else:
    print('NAO')