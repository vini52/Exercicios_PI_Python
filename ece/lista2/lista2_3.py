string = input()
first_word = []
sec_word = []


for i in range(len(string) - 1):
    if ' ' == string[i]:
        sec_word.append(string[i + 1:])
        break
    else:
        first_word.append(string[i])

sec = sec_word[0]
sec = list(sec)

if len(first_word) == len(sec):
    for j in range(len(sec)):
        print(first_word[j] + sec[j], end='')
elif len(first_word) < len(sec):
    for k in range(len(first_word)):
        print(first_word[k] + sec[k], end='')
    for l in range(len(first_word), len(sec)):
        print(sec[l], end='')
else:
    for k in range(len(sec)):
        print(first_word[k] + sec[k], end='')
    for l in range(len(sec), len(first_word)):
        print(first_word[l], end='')