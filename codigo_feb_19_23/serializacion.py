"""
Serialización en Python:
Librerías: pickle y shelve
"""

import pickle as p
import shelve as s
from fecha_hora import Date, Time, DateTime


def serializarPickle(path, obj):
    f = None
    try:
        f = open(path, "wb")
        p.dump(obj, f, protocol=2)
    except Exception as e:
        print(e)
    finally:
        if f:
            f.close()


def imprimir(L):
    for i in L:
        print(i, end=" ")
    print()


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


if __name__ == "__main__":
    L = [Date(1, 5, 2045), Time(12), DateTime()]
    imprimir(L)
    serializarPickle("../ficheros/ser_pickle.bin", L)
    L2 = deserializarPickle("../ficheros/ser_pickle.bin")
    imprimir(L2)
