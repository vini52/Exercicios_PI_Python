frase = input()

alfabeto = 'abcdefghijklmnopqrstuvwxyz'

cont = 0

frase = frase.lower()

for letra in alfabeto:
    for caracter in frase:
        if letra == caracter:
            cont += 1
            break
if cont == 26:
    print('SIM')
else:
    print('NAO')