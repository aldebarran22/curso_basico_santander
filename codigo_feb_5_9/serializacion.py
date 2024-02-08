"""
Serialización en Python con: pickle y shelve
Si tenemos 1 solo objeto: pickle
Si tenemos varios objetos: shelve (diccionario)
"""

import pickle as p
import shelve
from fecha_hora import DateTime, Time, Date


def serializarShelve(path, *objetos):
    Shelf = shelve.open(path)
    for k, i in enumerate(objetos):
        clave = f"K-{k}"
        Shelf[clave] = i
    Shelf.close()
    return len(objetos)


def serializarPickle(path, obj):
    fich = None
    try:
        fich = open(path, "wb")
        p.dump(obj, fich, 2)
    except Exception as e:
        print(e)
    finally:
        if fich:
            fich.close()


def deserializarPickle(path):
    fich = None
    try:
        fich = open(path, "rb")
        obj = p.load(fich)
        return obj
    except Exception as e:
        print(e)
    finally:
        if fich:
            fich.close()


if __name__ == "__main__":
    L = [DateTime(y=2020), DateTime(), DateTime(1, 12, 2000)]
    serializarPickle("exportaciones/datetime.bin", L)
    L2 = deserializarPickle("exportaciones/datetime.bin")
    for dt in L2:
        print(dt)

    dt = DateTime(1, 12, 2000)
    t = Time(12, 34, 56)
    d = Date(8, 9, 2024)
    serializarShelve("exportaciones/tiempo", dt, d, t)
