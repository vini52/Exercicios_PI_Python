palavra_a = input()
palavra_b = input()

cont = 0

for i in range(len(palavra_a)):
    if palavra_b == palavra_a[i:i+len(palavra_b)]:
        cont += 1
print(cont)