"""
Filtrar ficheros que cumplan unas condiciones.
"""
import os

L = os.listdir()
extensiones = ('txt','ipynb')
for f in L:
    ext = f.partition('.')[-1]
    if ext in extensiones:
        print(f)
