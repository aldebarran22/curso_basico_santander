"""
Listar los ficheros de una carpeta, pero sólo 2  
extensiones. Por ej: docx, xlsx... 
"""

import os

extensiones = ('py','pdf')
L = os.listdir()
for f  in L:
    ext = f.partition('.')[2]
    if ext in extensiones:
        print(f)