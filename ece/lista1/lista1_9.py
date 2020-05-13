equacao = input()

l = 0
r = 0
a = False

for caracter in equacao:
    if caracter == ')':
        r += 1
    elif caracter == '(':
        l += 1
    if r > l:
        print('Erro na parentizacao')
        a = True 
        break
if a == False:
    if l == r:
        print('Parentizacao correta')
    else:
        print('Erro na parentizacao')