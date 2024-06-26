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

def filtro2(*extensiones, path=None):
    return [fich for fich in os.listdir(path) \
            if fich.partition(".")[2] in extensiones]


if __name__ == "__main__":
    ficheros = filtro("pdf", path=r"D:\OneDrive\Escritorio\python_basico_santander\repositorio\doc")
    #ficheros = filtro("pdf", "xlsx", "html")

    ficheros2 = filtro2("pdf", path=r"D:\OneDrive\Escritorio\python_basico_santander\repositorio\doc")
    print(ficheros2)

    
