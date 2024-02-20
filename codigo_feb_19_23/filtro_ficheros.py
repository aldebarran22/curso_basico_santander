"""
A partir de una carpeta: listar el contenido, pero
solo imprimir ficheros de dos extensiones.
"""
import os

L = os.listdir("C:/")
extensiones = ('py','txt') 
for f in L:
    nombre, _, ext = f.partition('.')
    if ext in extensiones:
        print(f)



