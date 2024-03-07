"""
Serializar objetos con Python:
- pickle
- shelve
"""

import pickle as p
import shelve as s
from objetos import Candidato


def serializarShelve(path, *candidatos):
    Shelf = s.open(path)
    for pos, c in enumerate(candidatos):
        clave = f"K-{pos}"
        Shelf[clave] = c
    Shelf.close()


def serializarPickle(path, candidato):
    # Abrir el fichero para escritura en binario:
    fich = open(path, "wb")
    p.dump(candidato, fich)
    fich.close()


def deserializarPickle(path):
    # Abrir el fichero para lectura en binario:
    fich = open(path, "rb")
    obj = p.load(fich)
    print(obj)
    fich.close()


if __name__ == "__main__":
    c = Candidato("Andrés", 15, 9, True)
    c2 = Candidato("Sara", 22, 3, True)
    c3 = Candidato("Jaime", 2, 1, False)
    # serializarPickle("../ficheros/candidato.bin", c)
    # deserializarPickle("../ficheros/candidato.bin")
    serializarShelve("../ficheros/candidatos", c, c2, c3)
