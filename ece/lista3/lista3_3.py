notas = input().split(' ')
notas_conv = []

for i in notas:
    notas_conv.append(float(i))
menor = min(notas_conv)
maior = max(notas_conv)
notas_conv.remove(menor)
notas_conv.remove(maior)

soma = sum(notas_conv)
media = soma / len(notas_conv)

print('MEDIA FINAL: {:.4f}'.format(media))