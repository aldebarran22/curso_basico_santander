"""
Filtrar los ficheros de una carpeta a partir
de la extensión.
Buscar al menos dos extensiones distintas.
txt, csv
"""

import os

L = os.listdir()
extensiones = ("py", "xlsx")
for i in L:
    t = i.partition(".")
    if t[2] in extensiones:
        print(i)
