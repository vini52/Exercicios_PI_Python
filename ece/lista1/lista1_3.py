word = input()
num = int(input())

if num != 0:
    print(word, end='')
    for i in range(num-1):
        print(' , ' + word, end='')