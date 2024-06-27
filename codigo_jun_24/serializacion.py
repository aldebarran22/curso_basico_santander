"""
Serializar con pickle y shelve
"""

import pickle as p
import shelve as s

from objetos import Candidato


def serializarPickle(objeto, path):
    pass


def deserializarPickle(path):
    pass


def testPickle():
    c1 = Candidato("Pedro", 10, 6, True)


if __name__ == "__main__":
    testPickle()
