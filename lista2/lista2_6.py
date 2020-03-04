x = int(input())
y = int(input())
i = 2
soma = []
res = 0
while i <= x:
    if x % i == 0:
        div = x / i
        soma.append(div)
        res = sum(soma)
    i += 1
if res == y:
    print('amigos')
else:
    print('nao amigos')