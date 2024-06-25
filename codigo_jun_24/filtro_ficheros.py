"""
Implementar un filtro de ficheros. Filtrar ficheros de un par de
extensiones conocidas.
"""

import os


L = os.listdir()
for fich in L:
    ext = fich.partition(".")[2]
    if ext in ("pdf", "py"):
        print(ext)

