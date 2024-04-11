"""
Serialización de objetos con pickle y shelve
"""

import pickle as p
import shelve as s
from fecha_hora import Time, Date, DateTime


def serializarObjetos(path, *objetos):
    pass

def recuperarObjeto(path, key):
    pass

if __name__=='__main__':
    t1 = Time(12,30)
    d1 = Date(11,4,2024)
    dt = DateTime()

    serializarObjetos("../ficheros/obj_shelve", t1,d1,dt)