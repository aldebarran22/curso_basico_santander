"""
Serializar objetos con Python:
- pickle
- shelve
"""

import pickle as p
from objetos import Candidato


def serializarPickle(path, candidato):
    # Abrir el fichero para escritura en binario:
    fich = open(path, "wb")
    p.dump(candidato, fich)
    fich.close()


if __name__ == "__main__":
    c = Candidato("Andrés", 15, 9, True)
    serializarPickle("../ficheros/candidato.bin", c)
