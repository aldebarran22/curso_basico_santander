"""
Serializar con pickle y shelve
"""

import pickle as p
import shelve as s

from objetos import Candidato


def serializarPickle(objeto, path):
    fich = None
    try:
        fich = open(path, "wb")
        p.dump(objeto, fich)

    except Exception as e:
        print(e)

    finally:
        if fich:
            fich.close()


def deserializarPickle(path):
    pass


def testPickle():
    c1 = Candidato("Pedro", 10, 6, True)
    print(c1)
    serializarPickle(c1, "../ficheros/candidato.bin")
    c2 = deserializarPickle("../ficheros/candidato.bin")
    print(c2)


if __name__ == "__main__":
    testPickle()
