"""
Funciones del curso de  Python
"""

import os


def sumaResta(a,b):
    return a+b, a-b


def filtroFicheros(path, *extensiones):
    R = []
    L = os.listdir(path)
    # extensiones = ("py", "txt")
    for f in L:
        nombre, _, ext = f.partition(".")
        if ext in extensiones:
            R.append(f)
    return R


def histograma(L):
    d = dict()
    for i in set(L):
        d[i] = L.count(i)
    return d


if __name__ == "__main__":
    s,r = sumaResta(12,4)
    print("suma:",s,"resta:",r)

    print("ficheros:", filtroFicheros(".", "txt", "py", "xlsx", "pdf"))

    L = [1, 2, 3, 1, 1, 2, 3, 4, 5, 6, 3, 2, 1, 2]
    d = histograma(L)
    print(d)

    cad = "hola que tal"
    d2 = histograma(cad)
    print(d2)
