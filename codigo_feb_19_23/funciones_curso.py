"""
Funciones del curso de  Python
"""

import os
import math


def sumaResta(a, b):
    return a + b, a - b


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


def ecuacion(a, b, c):
    raiz = b**2 - 4 * a * c

    if raiz > 0:
        x1 = (-b + math.sqrt(raiz)) / (2 * a)
        x2 = (-b - math.sqrt(raiz)) / (2 * a)
        return {"x1": x1, "x2": x2}
        #return x1, x2
    else:
        return None


if __name__ == "__main__":
    d = ecuacion(1, 5, 4)
    print(d)
    d = ecuacion(1, 2, 3)
    print(d)

    s, r = sumaResta(12, 4)
    print("suma:", s, "resta:", r)

    print("ficheros:", filtroFicheros(".", "txt", "py", "xlsx", "pdf"))

    L = [1, 2, 3, 1, 1, 2, 3, 4, 5, 6, 3, 2, 1, 2]
    d = histograma(L)
    print(d)

    cad = "hola que tal"
    d2 = histograma(cad)
    print(d2)
