celsius = float(input("Digite a temperatura em Celsius: "))
if celsius < -273 or celsius > 4000:
    print("Temperatura digitada inválida!")
else:
    fahrenheit = round(celsius * 1.8 + 32,1)
    print(fahrenheit)