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


def serializarShelve(path, *objetos):
    Shelf = s.open(path)
    cont = 1
    for obj in objetos:
        clave = f"K-{cont}"
        Shelf[clave] = obj
        cont += 1
    Shelf.close()
    return len(objetos)


def deserializarShelve(path, numObjetos):
    Shelf = s.open(path)
    print("K-2", Shelf["K-2"])
    print("K-3", Shelf["K-3"])
    print("K-1", Shelf["K-1"])
    Shelf.close()


if __name__ == "__main__":
    L = [Date(1, 5, 2045), Time(12), DateTime()]
    imprimir(L)
    serializarPickle("../ficheros/ser_pickle.bin", L)
    L2 = deserializarPickle("../ficheros/ser_pickle.bin")
    imprimir(L2)
    ##################
    numObjs = serializarShelve("../ficheros/ser_shelve", *L)
    deserializarShelve("../ficheros/ser_shelve", numObjs)
