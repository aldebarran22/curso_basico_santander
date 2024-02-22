"""
Operaciones con ficheros en Python
"""

import sys


def leerFichero(path):
    f = None
    try:
        f = open(path, "r")
        for linea in f:
            linea = linea.rstrip()
            print(linea)

    except Exception as e:
        print(e)

    finally:
        if f:
            f.close()


def isFloat(num):
    if type(num) == str:
        return num.replace(".", "").isnumeric()
    else:
        return 0.0


def filtroFichero(path, *paises, sep=";", file=sys.stdout):
    f = None
    cabs = False
    try:
        f = open(path, "r")
        for linea in f:
            linea = linea.rstrip()
            if not cabs:
                cabs = True
                print(linea, file=file)
            else:
                columnas = linea.split(sep)
                if isFloat(columnas[-2]):
                    columnas[-2] = columnas[-2].replace(".", ",")

                if columnas[-1] in paises:
                    print(sep.join(columnas), file=file)

    except Exception as e:
        print(e)

    finally:
        if f:
            f.close()


def columnas():
    L = [('portatil', 550.7), ('PC', 1550.0), ('teclado', 40.79)]
    for producto, importe in L:
        print("%-10s\t%7.2f" % (producto, importe))

if __name__ == "__main__":

    # leerFichero("../ficheros_curso/Pedidos.txt")

    """
    f = open("../csv/pedidos.csv", "w")
    filtroFichero("../ficheros_curso/Pedidos.txt", "Suiza", file=f)
    f.close()
    """

    columnas()
