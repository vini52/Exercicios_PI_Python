word = input()

vogais = 'aeiou'

for letra in word:
    for i in range(len(vogais)):
        if letra == vogais[i] or letra == vogais[i].upper():
            word = word.replace(letra, '')
print(word)