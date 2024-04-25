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


def fusion(path1, path2, pathDestino):

    def csv_to_set(path):
        """Leer un fichero de empleados y lo devuelve en un 
        conjunto de filas"""
        f= None
        try:
            f = open(path, "r")
            csv = f.read()
            return set(csv.split("\n"))

        except Exception as e:
            print(e.__class__.__name__, e)

        finally:
            if f: f.close()

    def criterio(fila):
        t = fila.partition(";")
        if t[0].isnumeric():
            return int(t[0])
        else:
            return 0

    # cuerpo de la funcion: fusionFicheros
    c1 = csv_to_set(path1)
    c2 = csv_to_set(path2)
    todo = c1 | c2  # La unión a nivel de filas
    L = sorted(todo, key=criterio)
    return "\n".join(L)

def fusionFicheros(csv1, csv2):

    def csv_to_set(csv):
        return set(csv.split("\n"))

    def criterio(fila):
        t = fila.partition(";")
        if t[0].isnumeric():
            return int(t[0])
        else:
            return 0

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


def testFusion():
    csv = fusion("../ficheros_curso/Empleados2.txt",
    "../ficheros_curso/Empleados3.txt",
    "../ficheros/empleados_todo.txt")
    print(csv)

if __name__ == "__main__":
    # testFiltroFicheros()
    # testHistograma()
    # testFusionFicheros()
    testFusion()
