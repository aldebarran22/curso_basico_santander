"""
Funciones del curso de  Python
"""


def histograma(L):
    d = dict()
    for i in set(L):
        d[i] = L.count(i)
    return d


if __name__ == "__main__":
    L = [1, 2, 3, 1, 1, 2, 3, 4, 5, 6, 3, 2, 1, 2]
    d = histograma(L)
    print(d)

    cad = "hola que tal"
    d2 = histograma(cad)
    print(d2)