import math

numero_de_elementos = int(input().split("n = ")[1])

frase = input().split("Vetor X: ")[1]
vetor_x = list()
for numero in frase.split(" "):
  vetor_x.append(float(numero))

media = (sum(vetor_x)) / (len(vetor_x))
somatoria = 0

for i in range(numero_de_elementos):
    somatoria += (math.pow((vetor_x[i] - media), 2)) * vetor_x[i]
somatoria = somatoria * (1 / (numero_de_elementos * numero_de_elementos))
hagrid = math.sqrt(somatoria)

print('Hagrid = {:.2f}'.format(hagrid))