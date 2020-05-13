ra = input()
senha = []
ra = list(ra)
if ra[0] != 'R' or len(ra) < 20:
    print('RA INVALIDO')
else:
    for i in range(2, len(ra)):
        if ra[i] != '0':
            indice = i
            break
    for j in range(indice, len(ra)):
        senha.append(ra[j])

print(''.join(map(str, senha)))