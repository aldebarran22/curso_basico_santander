"""
Serializar objetos con Python:
- pickle
- shelve
"""

import pickle as p
from objetos import Candidato


def serializarPickle(path, candidato):
    pass


if __name__ == "__main__":
    c = Candidato("Andrés", 15, 9, True)
    serializarPickle("../ficheros/candidato.bin", c)
