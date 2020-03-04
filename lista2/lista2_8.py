n = int(input())
primos = 0
for i in range(n):
    div = 0
    num = int(input())
    cont = 1
    while cont <= num:
        if num % cont == 0:
            div += 1
        cont += 1
    if div == 2:
        primos += 1
print('dos {} numeros informados {} eram primos'.format(n,primos))