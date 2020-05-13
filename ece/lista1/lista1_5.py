palavra = input()
palavra = palavra.lower()
palavra = list(palavra)
if palavra == palavra[::-1]:
    print('PALINDROMO')
else:
    print('NAO EH PALINDROMO')