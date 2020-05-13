numero_de_elementos = int(input().split("n = ")[1])

frase_x = input().split("Vetor X: ")[1]
frase_y = input().split("Vetor Y: ")[1]
vetor_x = []
vetor_y = []

for numero in frase_x.split(" "):
    vetor_x.append(float(numero))
for numero in frase_y.split(" "):
    vetor_y.append(float(numero))

convolucao = 0

for i in range(numero_de_elementos):
    convolucao += (vetor_x[i] * (vetor_y[numero_de_elementos-1 - i]))
print('Convolucao = {:.2f}'.format(convolucao))