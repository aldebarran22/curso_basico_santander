"""
Generar un histograma con una lista de valores aleatorios.
"""

import matplotlib.pyplot as plt
import random

def generarHisto(N=1000,ini=1,fin=20):

    # Generar una lista con N números aleatorios:
    L = []
    for i in range(N):
        L.append(random.randint(ini, fin))

    claves = set(L)
    histograma = dict()
    for num in claves:
        histograma[num] = L.count(num)

    return histograma



if __name__ == '__main__':
    histograma = generarHisto(500, 1, 15)
    x = histograma.keys()
    y = histograma.values()

    plt.plot(x, y)
    plt.show()

    #for k, v in histograma.items():
    #    print(k,v)