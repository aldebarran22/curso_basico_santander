"""
Serializar con python:
pickle -> 1 objeto
shelve -> varios objetos (diccionario)
"""

from random import randint
from string import ascii_letters

import pickle as p
import shelve as s


def serializarPickle(path, obj):
    f = None
    try:
        f = open(path, "wb")
        p.dump(obj, f, 2)

    except Exception as e:
        print(e)

    finally:
        if f:
            f.close()


def deserializarPickle(path):
    f = None
    try:
        f = open(path, "rb")
        obj = p.load(f)
        return obj

    except Exception as e:
        print(e)

    finally:
        if f:
            f.close()


def generarDict():
    # Generar una estructura aleatoria, lista de diccionarios, cada dicc representa un candidato.
    candidatos = [
        {
            "nombre": letra * 5,
            "exp": randint(2, 8),
            "emp": randint(1, 6),
            "sup": True if randint(1, 10) % 2 == 0 else False,
        }
        for letra in ascii_letters
    ]
    return candidatos


if __name__ == "__main__":
    cand = generarDict()
    serializarPickle("../ficheros/cand_pickle.dat", cand)
    cand2 = deserializarPickle("../ficheros/cand_pickle.dat")
    print(cand == cand2)
