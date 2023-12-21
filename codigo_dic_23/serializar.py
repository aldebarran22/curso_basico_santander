"""
Serializar un lista de objetos y deserializar
"""
import pickle as p
import shelve
from objetos import Persona
from random import randint


def serializar(path, L):
    f = None
    try:
        f = open(path, "wb")
        p.dump(L, f, 2)

    except Exception as e:
        print(e)
    finally:
        if f:
            f.close()


def deserializar(path):
    f = None
    try:
        f = open(path, "rb")
        L = p.load(f)
        return L

    except Exception as e:
        print(e)
    finally:
        if f:
            f.close()


def generarLista():
    L = []
    for i in range(65, 65 + 26):
        p = Persona(chr(i) * 3, randint(18, 65), randint(160, 190) / 100)
        L.append(p)
    return L


def testPickle():
    serializar("personas.dat", L)
    L2 = deserializar("personas.dat")
    for p in L2:
        print(p)


def serializarShelve(path, L):
    shelf = shelve.open(path)
    for obj in L:
        shelf[obj.nombre] = obj
    shelf.close()


def deserializarShelve(path):
    shelf = shelve.open(path)
    print(shelf["CCC"])
    print(shelf["AAA"])
    print(shelf["BBB"])
    shelf.close()


def testShelve(L):
    serializarShelve("personal", L)
    deserializarShelve("personal")

if __name__ == "__main__":
    L = generarLista()
    testShelve(L[:3])
