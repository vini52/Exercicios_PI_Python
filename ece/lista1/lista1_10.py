num = int(input())
maior = 0
for i in range(num):
    linha = input()
    palavra = 0 
    for i in range(len(linha)):
        if linha[i] == ' ' or linha[i] == '.' or linha[i] == ',' or linha[i] == '!' or linha[i] == '?':
            if palavra < maior:
                palavra = 0
            else:
                maior = palavra
                palavra = 0
        else:
            palavra += 1
    if palavra > maior:
        maior = palavra
print('Tam. Maior Palavra: {}'.format(maior))