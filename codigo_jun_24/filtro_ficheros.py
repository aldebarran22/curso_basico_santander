"""
Implementar un filtro de ficheros. Filtrar ficheros de un par de
extensiones conocidas.
"""

import os


def filtro(*extensiones):
    L = os.listdir("")
    for fich in L:
        ext = fich.partition(".")[2]
        if ext in extensiones:
            print(fich)


if __name__ == "__main__":
    ficheros = filtro("pdf")
    ficheros = filtro("pdf", "xlsx", "html")
