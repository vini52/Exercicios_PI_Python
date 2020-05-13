import matplotlib.pyplot as plt
import matplotlib.image as mpimg

foto = mpimg.imread('img/print.png')
linhas = len(foto)
colunas = len(foto[0])

for i in range(linhas):
    for j in range(colunas):
        foto[i,j][1] = foto[i,j][1] / 2
        foto[i,j][2] = foto[i,j][2] / 2
plt.imshow(foto)
plt.show()