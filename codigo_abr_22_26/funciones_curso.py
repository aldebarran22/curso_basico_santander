"""
Funciones del curso:
- Filtro de ficheros (por extensión)
"""

import os

# from os import listdir

import random

emp2 = """id;nombre;cargo
1;Davolio;Representante de ventas
2;Fuller;Vicepresidente comercial
3;Leverling;Representante de ventas
4;Peacock;Representante de ventas
6;Suyama;Representante de ventas
7;King;Representante de ventas
9;Dodsworth;Representante de ventas"""


emp3 = """id;nombre;cargo
2;Fuller;Vicepresidente comercial
3;Leverling;Representante de ventas
4;Peacock;Gerente de ventas
5;Buchanan;Gerente de ventas
6;Suyama;Representante de ventas
7;King;Representante de ventas
8;Callahan;Coordinador ventas interno
9;Dodsworth;Representante de ventas
10;George;Representante de ventas"""


def fusionFicheros(csv1, csv2):

    def csv_to_set(csv):
        return set(csv.split("\n"))
    
    def criterio(fila):
        return fila

    # cuerpo de la funcion: fusionFicheros
    c1 = csv_to_set(csv1)
    c2 = csv_to_set(csv2)
    todo = c1 | c2  # La unión a nivel de filas
    L = sorted(todo, key=criterio)
    return "\n".join(L)


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
    # L = []
    # histo = dict()

    # Almacenar n números aleatorios en la lista L
    # for i in range(n):
    #    L.append(random.randint(ini, fin))
    L = [random.randint(ini, fin) for _ in range(n)]

    # Quitar los repetidos y almacenarlos en un conjunto
    numeros = set(L)

    # Contar los valores del conjunto en la lista y almacenar
    # en el diccionario (la clave -> el número), (el valor -> el recuento)
    # for i in numeros:
    #    histo[i] = L.count(i)

    histo = {i: L.count(i) for i in numeros}

    L = sorted(histo.items(), key=lambda t: t[1], reverse=True)
    return L


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
    for numero, cuenta in histo:
        print(f"{numero} se repite {cuenta} veces")


def testFusionFicheros():
    csvFinal = fusionFicheros(emp2, emp3)
    print(csvFinal)


if __name__ == "__main__":
    # testFiltroFicheros()
    # testHistograma()
    testFusionFicheros()
