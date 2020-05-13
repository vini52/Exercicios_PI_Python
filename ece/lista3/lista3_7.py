direcao = input()
palavra = input()
print(f'Lista : {palavra}')
palavra_vet = palavra.split(' ')
cont = 1
rotacao = []

if direcao == 'E' and len(palavra_vet) > 1:
    for i in range(len(palavra_vet)-1):
        rotacao.append(palavra_vet[len(palavra_vet)-1])
        for j in range(len(palavra_vet)-1):
            rotacao.append(palavra_vet[j])
        rot_final = ''
        for caracter in rotacao:
            rot_final += caracter
            rot_final += ' '
        print(f'Rotacao {cont}: {rot_final}')
        cont += 1
        palavra_vet = []
        palavra_vet = rotacao
        rotacao = []
elif direcao == 'D' and len(palavra_vet) > 1:
    for i in range(len(palavra_vet)-1):
        for j in range(1, len(palavra_vet)):
            rotacao.append(palavra_vet[j])
        rotacao.append(palavra_vet[0])
        rot_final = ''
        for caracter in rotacao:
            rot_final += caracter
            rot_final += ' '
        print(f'Rotacao {cont}: {rot_final}')
        cont += 1
        palavra_vet = []
        palavra_vet = rotacao
        rotacao = []
else:
    print('NENHUMA ROTACAO POSSIVEL')