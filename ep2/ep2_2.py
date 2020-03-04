altura = float(input())
peso = float(input())
imc = peso / ((altura / 100) ** 2)
if imc <= 18.5:
    print('Magro')
elif imc <= 25:
    print('Saudavel')
elif imc <= 30:
    print('Acima do peso')
elif imc <= 35:
    print('Obeso')
else:
    print('Morbidez')