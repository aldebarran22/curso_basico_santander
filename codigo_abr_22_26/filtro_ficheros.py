"""
Imprimir los ficheros de una carpeta
que sean de extensión "txt" o "png"
"""

import os

L = os.listdir("../ficheros")
extensiones = ("txt", "png")
for f in L:
    t = f.partition(".")
    ext = t[2]
    if ext in extensiones:
        print(f)

""" Bucle infinito: cortar con CONTROL+C
while True:
    pass
"""
