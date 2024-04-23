"""
Funciones del curso:
- Filtro de ficheros (por extensión)
"""

import os

L = os.listdir("../ficheros")
extensiones = ("txt", "png")
for f in L:
    t = f.partition(".")
    ext = t[2]
    if ext in extensiones:
        print(f)

if __name__ == "__main__":
    L = filtroFicheros(path, "txt")
    L = filtroFicheros(path, "txt", "py")
    L = filtroFicheros(path, "txt", "png", "py")

    t = ("txt", "py")
    L = filtroFicheros(path, *t)
