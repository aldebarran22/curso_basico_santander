"""
Imprimir los ficheros de una carpeta
que sean de extensión "txt" o "png"
"""

import os

L = os.listdir()
extensiones = ("txt", "png")
for f  in L:
    ext = f.partition('.')[2]
    if ext in extensiones:
        print(f)

