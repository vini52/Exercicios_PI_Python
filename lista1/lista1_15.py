a = float(input())
b = float(input())
c = float(input())
lista = [a,b,c]
lista.sort()
a = lista[2]
b = lista[1]
c = lista[0]
if a >= b + c:
    print("NAO FORMA TRIANGULO")
else:
    if a * a == b * b + c * c:
        print("TRIANGULO RETANGULO")
    if a * a > b * b + c * c:
        print("TRIANGULO OBTUSANGULO")
    if a * a < b * b + c * c:
        print("TRIANGULO ACUTANGULO")
    if a == b and b == c:
        print("TRIANGULO EQUILATERO")
    elif a == b or a == c or b == c:
        print("TRIANGULO ISOSCELES")