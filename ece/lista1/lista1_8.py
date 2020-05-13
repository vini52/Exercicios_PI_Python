frase = input()
frase = frase.lower()

vogais = 'aeiou'
consoantes = 'bcdfghjklmnpqrstvwxyz'
espaco = ' '
pontuacao = ".,'!?"

num_char = len(frase)
v = 0
c = 0
e = 0 
p = 0

for i in range(len(frase)):
    for j in range(len(vogais)):
        if frase[i] == vogais[j]:
            v += 1
for i in range(len(frase)):
    for j in range(len(consoantes)):
        if frase[i] == consoantes[j]:
            c += 1
for i in range(len(frase)):
    for j in range(len(espaco)):
        if frase[i] == espaco[j]:
            e += 1
for i in range(len(frase)):
    for j in range(len(pontuacao)):
        if frase[i] == pontuacao[j]:
            p += 1

percent_vogais = (v / num_char) * 100
percent_consoantes = (c / num_char) * 100
percent_espaco = (e / num_char) * 100
percent_pontuacao = (p / num_char) * 100

print('Vogais: {:.2f}%'.format(percent_vogais))
print('Consoantes: {:.2f}%'.format(percent_consoantes))
print('Espacos: {:.2f}%'.format(percent_espaco))
print('Pontuacoes: {:.2f}%'.format(percent_pontuacao))