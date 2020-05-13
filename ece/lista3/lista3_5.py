def numeros(n:int) -> list:
    lista = []
    for i in range(n):
        lista.append(float(input()))
    return lista

def media(lista:list) ->  float:
    media = 0
    parcial = 0
    for i in range(len(lista)):
        parcial += lista[i]
        print('parcial - {:.2f}'.format(parcial))
    media = parcial / len(lista)
    print('media - {:.2f}'.format(media))
    return media

def variancia(lista:list, media:float):
    parcial = 0
    variancia = 0
    for i in range(len(lista)):
        parcial += (lista_num[i] - media) * (lista[i] - media)
        print('parcial - {:.2f}'.format(parcial))
    variancia = (parcial / (len(lista) - 1))
    print('variancia - {:.2f}'.format(variancia))


num = int(input())
lista_num = numeros(num)
media = media(lista_num)
variancia = variancia(lista_num, media)