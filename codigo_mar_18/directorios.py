"""Explorar directorios"""

from os import walk


def ls(ruta="."):
    # Devuelve una tupla de 3 elementos.
    dir, subdirs, archivos = next(walk(ruta))
    print("Actual: ", dir)
    print("Subdirectorios: ", subdirs)
    print("Archivos: ", archivos[:3])  # Devuelve la lista de

    for subdir in subdirs:
        ls(dir + "/" + subdir)
        print("*" * 30)


if __name__ == "__main__":
    ls()
