"""
Serialización de objetos con pickle y shelve
"""

import pickle as p
import shelve as s
from fecha_hora import Time, Date, DateTime


def serializarObjetos(path, *objetos):
    Shelf = s.open(path)
    for pos, obj in enumerate(objetos):
        clave = f"K-{pos}"
        Shelf[clave] = obj

    Shelf.close()

def recuperarObjeto(path, key):
    Shelf = s.open(path)
    print(list(Shelf.keys()))
    print(list(Shelf.values()))
    obj = Shelf[key]
    Shelf.close()
    return obj

if __name__=='__main__':
    t1 = Time(12,30)
    d1 = Date(11,4,2024)
    dt = DateTime()

    serializarObjetos("../ficheros/obj_shelve", t1,d1,dt)
    obj = recuperarObjeto("../ficheros/obj_shelve", "K-1")
    print(obj)