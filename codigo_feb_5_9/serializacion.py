"""
Serialización en Python con: pickle y shelve
Si tenemos 1 solo objeto: pickle
Si tenemos varios objetos: shelve (diccionario)
"""

import pickle as p
import shelve
from fecha_hora import DateTime


def serializarPickle(path, obj):
    pass


def deserializarPickle(path):
    pass


if __name__ == "__main__":
    L = [DateTime(y=2020), DateTime(), DateTime(1, 12, 2000)]
