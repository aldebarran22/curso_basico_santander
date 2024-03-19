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

print(filtroFicheros('py','txt', path='.'))
print(filtroFicheros('txt', path='.'))

