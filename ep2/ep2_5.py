a = int(input())
b = int(input())
c = int(input())
if a >= b + c or b >= a + c or c >= a + b:
    print('INVALIDO')
else:
    print('VALIDO')
