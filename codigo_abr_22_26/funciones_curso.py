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


def histograma(n=1000, ini=1, fin=20):
    L = []
    histo = dict()

    # Almacenar n números aleatorios en la lista L
    for i in range(n):
        L.append(random.randint(ini, fin))

    # Quitar los repetidos y almacenarlos en un conjunto
    numeros = set(L)

    # Contar los valores del conjunto en la lista y almacenar
    # en el diccionario (la clave -> el número), (el valor -> el recuento)
    for i in numeros:
        histo[i] = L.count(i)

    return histo


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
    histo = histograma()
    # Imprimir resultados:
    for numero, cuenta in histo.items():
        print(f"{numero} se repite {cuenta} veces")


if __name__ == "__main__":
    # testFiltroFicheros()
    testHistograma()
