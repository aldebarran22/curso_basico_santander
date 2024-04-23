"""
Funciones del curso:
- Filtro de ficheros (por extensión)
"""

import os
import random


def filtroFicheros(*extensiones, path=None):
    R = list()
    L = os.listdir(path)
    for f in L:
        t = f.partition(".")
        ext = t[2]
        if ext in extensiones:
            R.append(f)
    return R


def histograma():
    n = 1000
    L = []
    histo = dict()
    # El intervalo de números:
    ini = 1
    fin = 20

    # Almacenar n números aleatorios en la lista L
    for i in range(n):
        L.append(random.randint(ini, fin))
   
    # Quitar los repetidos y almacenarlos en un conjunto
    numeros = set(L)
   
    # Contar los valores del conjunto en la lista y almacenar
    # en el diccionario (la clave -> el número), (el valor -> el recuento)
    for i in numeros:
        histo[i] = L.count(i)

def testFiltroFicheros():
    L = filtroFicheros("txt")
    print(L)
    L = filtroFicheros("txt", "png")
    print(L)
    # L = filtroFicheros("txt", "png", "py")

    t = ("txt", "py")
    L = filtroFicheros(*t, path="../ficheros_curso")
    print(L)


def testHistograma():
    pass


if __name__ == "__main__":
    testFiltroFicheros()
    #testHistograma()
