"""
Filtrar los ficheros de una o más extensiones
de una carpeta
"""

import os

L = os.listdir()
for f in L:
    ext = f.partition(".")[2]
    if ext in ("txt", "py"):
        print(f)
