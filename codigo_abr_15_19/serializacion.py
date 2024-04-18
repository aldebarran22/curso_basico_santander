"""
Serializar objetos con pickle y shelve

pickle: para un solo objeto OK!
shelve: mejor para varios objetos, se puede tratar como si fuera un dict.
"""

import pickle as p
import shelve as s


def serializarPickle(path, obj):
    """Serializa un objeto con pickle"""
    fich = None
    try:
        fich = open(path, "wb")

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

    except Exception as e:
        print(e.__class__.__name__, e)

    finally:
        if fich != None:
            fich.close()
