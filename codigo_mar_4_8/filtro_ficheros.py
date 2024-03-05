"""
Listar los ficheros de una carpeta del equipo e imprimir
solo los ficheros de una determinada extensión.
"""
import os

L = os.listdir('../ficheros_curso')
for fich in L:
    ext = fich.partition('.')[2]
    if ext == 'csv':
        print(fich)