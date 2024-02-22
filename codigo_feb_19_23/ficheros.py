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


def filtroFichero(path, *paises, sep=";", file=sys.stdout):
    f = None
    try:
        f = open(path, "r")
        for linea in f:
            linea = linea.rstrip()
            columnas = linea.split(sep)
            if columnas[-1] in paises:
                print(linea, file=file)

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


if __name__ == "__main__":
    print(isFloat("12.44"))
    print(isFloat("12"))
    print(isFloat("12h"))
    # leerFichero("../ficheros_curso/Pedidos.txt")

    f = open("../csv/pedidos.csv", "w")
    filtroFichero("../ficheros_curso/Pedidos.txt", "Finlandia", "Alemania", file=f)
    f.close()
