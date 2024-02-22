"""
Gestión de directorios: walk
"""

from os import walk

directorio, subdirectorios, ficheros = next(walk("."))
print('Dir:', directorio)
print('Sub:', subdirectorios)
print("Ficheros:", len(ficheros))