dia1 = int(input())
mes1 = int(input())
ano1 = int(input())
dia2 = int(input())
mes2 = int(input())
ano2 = int(input())
if ano1 < ano2:
    print('DATA1')
elif ano1 == ano2 and mes1 < mes2:
    print('DATA1')
elif ano1 == ano2 and mes1 == mes2 and dia1 < dia2:
    print('DATA1')
elif ano1 == ano2 and mes1 == mes2  and dia1 == dia2:
    print('IGUAIS')
else:
    print('DATA2')