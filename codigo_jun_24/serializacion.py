"""
Serializar con pickle y shelve
"""

import pickle as p
import shelve as s

from objetos import Candidato
from fecha_hora import Date, Time, DateTime


def serializarPickle(objeto, path):
    fich = None
    try:
        fich = open(path, "wb")
        p.dump(objeto, fich)

    except Exception as e:
        print(e)

    finally:
        if fich:
            fich.close()


def deserializarPickle(path):
    # Abrir fichero en modo rb:
    fich = None
    try:
        fich = open(path, "rb")
        objeto = p.load(fich)
        return objeto

    except Exception as e:
        print(e)

    finally:
        if fich:
            fich.close()


def testPickle():
    c1 = Candidato("Pedro", 10, 6, True)
    print(c1)
    serializarPickle(c1, "../ficheros/candidato.bin")
    c2 = deserializarPickle("../ficheros/candidato.bin")
    print(c2)


def serializarShelve(path, *objetos):
    Shelf = s.open(path)
    for pos, obj in enumerate(objetos):
        clave = f"K-{pos+1}"
        Shelf[clave] = obj

    Shelf.close()


def deserializarShelve(path, clave):
    pass


def testShelve():
    c1 = Candidato("Pedro", 10, 6, True)
    fecha = Date(23, 6, 2024)
    hora = Time(8, 55, 4)
    fechaHora = DateTime(1, 3, 2000, 12, 34, 5)

    serializarShelve("../ficheros/objetos", c1, fecha, hora, fechaHora)

    obj1 = deserializarShelve("../ficheros/objetos", "K-2")
    print(obj1)
    obj2 = deserializarShelve("../ficheros/objetos", "K-4")
    print(obj2)


if __name__ == "__main__":
    # testPickle()
    testShelve()
