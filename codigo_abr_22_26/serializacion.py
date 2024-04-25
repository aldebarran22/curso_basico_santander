"""
Serialización en Python
pickle: para un solo objeto ok!
shelve: para varios objetos --> utiliza un diccionario
para acceder directamente a los objetos.
"""

import pickle as p
import shelve as s

from random import randint
from fecha_hora import Time, Date, DateTime

def serializarPickle(path, objeto):
    f = None
    try:
        f = open(path, "wb")
        p.dump(objeto, f)

    except Exception as e:
        print(e)

    finally:
        if f: f.close()

def deserializarPickle(path):
    f = None
    try:
        f = open(path, "rb")
        objeto = p.load(f)
        return objeto

    except Exception as e:
        print(e)

    finally:
        if f: f.close()

def  serializarShelve(path, *objetos):
    Shelf = s.open(path)
    for obj in objetos:
        clave = obj.__class__.__name__
        valor = obj

        Shelf[clave] = obj

    Shelf.close()

def deserializarShelve(path, clave):
    Shelf = s.open(path)
    obj = Shelf.get(clave, f"No existe la clave: {clave}") 
    Shelf.close()
    return obj


if __name__ == '__main__':
    L = [Time(randint(0,23), randint(0, 59)) for _ in range(20)]
    print(L[:3])
    serializarPickle("../ficheros/objetos_pickle.dat", L)
    L2 = deserializarPickle("../ficheros/objetos_pickle.dat")
    print(L2[:3])

    # Serializar con shelve
    clases = [Time, Date, DateTime]
    objetos = [c() for c in clases]
    print(objetos)

    serializarShelve("../ficheros/tiempo2", *objetos)
    objeto = deserializarShelve("../ficheros/tiempo", "Time2")
    print(objeto)

