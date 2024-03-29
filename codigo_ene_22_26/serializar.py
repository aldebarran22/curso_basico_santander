"""
Serializar objetos con pickle: para 1 sólo objeto y shelve: para varios
Se puede tratar como un diccionario
"""
import pickle as p
import shelve
from fecha_hora import DateTime, Date, Time


def serializarShelve(nombreFichero, *args):
    Shelf = shelve.open(nombreFichero)
    k = 1
    for obj in args:
        clave = f"k-{k}"
        Shelf[clave] = obj
        k += 1
    Shelf.close()
    return k


def deserializarShelve(nombreFichero, numClaves):
    Shelf = shelve.open(nombreFichero)
    for k in range(1, numClaves):
        clave = f"k-{k}"
        print(clave, Shelf[clave])
    Shelf.close()


def serializarPickle(path, objeto):
    fich = None
    try:
        # Abrir el fichero binario para escritura
        fich = open(path, "wb")
        p.dump(objeto, fich, 2)

    except Exception as e:
        print(e)
    finally:
        if fich:
            fich.close()


def deserializarPickle(path):
    fich = None
    try:
        # Abrir el fichero binario para lectura
        fich = open(path, "rb")
        objeto = p.load(fich)
        return objeto

    except Exception as e:
        print(e)
    finally:
        if fich:
            fich.close()


if __name__ == "__main__":
    L = [DateTime(), DateTime(y=2000), DateTime(1, 5, 2023)]
    serializarPickle("fecha_hora.bin", L)
    L2 = deserializarPickle("fecha_hora.bin")
    print(L)
    print(L2)

    t1 = Time(12, 3, 4)
    d1 = Date(8, 9, 2023)
    numClaves = serializarShelve("tiempo", t1, d1)
    deserializarShelve("tiempo", numClaves)
