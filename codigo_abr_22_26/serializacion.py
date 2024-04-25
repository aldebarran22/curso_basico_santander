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


if __name__ == '__main__':
    L = [Time(randint(0,23), randint(0, 59)) for _ in range(20)]
    print(L[:3])
    serializarPickle("../ficheros/objetos_pickle.dat")
    
