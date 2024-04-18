"""
Serializar objetos con pickle y shelve

pickle: para un solo objeto OK!
shelve: mejor para varios objetos, se puede tratar como si fuera un dict.
"""

import pickle as p
import shelve as s
from fecha_hora import Date, Time


def serializarShelve(path, *objetos):
    Shelf = s.open(path)
    k = 1
    for obj in objetos:
        clave = f"K-{k}"
        k += 1
        Shelf[clave] = obj

    Shelf.close()


def serializarPickle(path, obj):
    """Serializa un objeto con pickle"""
    fich = None
    try:
        fich = open(path, "wb")
        p.dump(obj, fich)

    except Exception as e:
        print(e.__class__.__name__, e)

    finally:
        if fich != None:
            fich.close()


def deserializarPickle(path):
    """Deserializa un objeto con pickle"""
    fich = None
    try:
        fich = open(path, "rb")
        obj = p.load(fich)
        return obj

    except Exception as e:
        print(e.__class__.__name__, e)

    finally:
        if fich != None:
            fich.close()


def deserializarShelve(path, clave):
    Shelf = s.open(path)
    print("Claves: ", list(Shelf.keys()))
    if clave in Shelf:
        obj = Shelf[clave]
    else:
        obj = None
    Shelf.close()
    return obj


if __name__ == "__main__":
    t = Time(12, 34)
    d = Date(15, 4, 2024)
    L = [d, t]
    print(L[0], L[1])

    serializarPickle("../ficheros/pickle_obj.bin", L)
    L2 = deserializarPickle("../ficheros/pickle_obj.bin")
    print(L2[0], L2[1])

    serializarShelve("../ficheros/objetos_shelve", d, t, [1, 2, 3, 4, 5])

    obj1 = deserializarShelve("../ficheros/objetos_shelve", "K-1")
    print(obj1)
