"""
Funciones del curso:
- Filtro de ficheros (por extensión)
"""

import os


def filtroFicheros(*extensiones, path=None):
    R = list()
    L = os.listdir(path)
    for f in L:
        t = f.partition(".")
        ext = t[2]
        if ext in extensiones:
            R.append(f)
    return R


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
