"""
Funciones en Python
"""

import os


def filtroFicheros(*extensiones, path=None):
    L = os.listdir(path)
    R = []
    for f in L:
        ext = f.partition(".")[2]
        if ext in extensiones:
            R.append(f)
    return R

if __name__ == '__main__':
    print(__name__)
    print(filtroFicheros("py", "txt", path="."))
    print(filtroFicheros("txt", path="."))
    ext = ("py", "txt")
    print(filtroFicheros(*ext))
