num = int(input())
lista = []

for i in range(num):
    palavra = input()
    lista.append(palavra)
lista.reverse()
for j in range(num):
    print(lista[j])