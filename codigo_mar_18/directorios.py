"""Explorar directorios"""

from os import walk
def ls (ruta = "."):
    #Devuelve una tupla de 3 elementos.
    dir, subdirs , archivos = next(walk(ruta))
    print("Actual: ", dir)
    print("Subdirectorios: ", subdirs)
    print("Archivos: ", archivos) # Devuelve la lista de

if __name__ == '__main__':
    ls()