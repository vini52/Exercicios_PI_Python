temperatura = float(input())
if temperatura < -20:
    print('Muito Baixa')
elif temperatura <= 30:
    print('Baixa')
elif temperatura <= 200:
    print('Normal')
elif temperatura <= 250:
    print('Alta')
else:
    print('Muito Alta')