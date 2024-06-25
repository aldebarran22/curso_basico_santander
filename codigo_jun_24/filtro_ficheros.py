"""
Implementar un filtro de ficheros. Filtrar ficheros de un par de
extensiones conocidas.
"""

import os


def filtro(*extensiones, path=None):
    #rpath = path.replace("\\","/")
    L = os.listdir(path)
    for fich in L:
        ext = fich.partition(".")[2]
        if ext in extensiones:
            print(fich)


if __name__ == "__main__":
    ficheros = filtro("pdf", path=r"D:\OneDrive\Escritorio\python_basico_santander\repositorio\doc")
    #ficheros = filtro("pdf", "xlsx", "html")

    
