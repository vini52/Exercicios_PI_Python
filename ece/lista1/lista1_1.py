letter = input()
letter_upper = letter.upper()
word = input()
word = word.replace(letter, '')
word = word.replace(letter_upper, '')
print(word)
