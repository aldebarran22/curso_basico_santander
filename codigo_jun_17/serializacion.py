"""
Serialización. Librerías: pickle y shelve
"""
import pickle as p
import shelve as s

from objetos import Producto
from fecha_hora import Date, Time, DateTime

def serializarPickle(path, objeto):
    fich = open(path, "wb") # Abrir para escritura en binario
    p.dump(objeto, fich)
    fich.close()

def deserializarPickle(path):
    fich = open(path, "rb")
    obj = p.load(fich)
    fich.close()
    return obj

def serializarShelve(path, **objetos):
    Shelf = s.open(path)
    for k, v in objetos.items():
        Shelf[k] = v
    Shelf.close()


if __name__ == '__main__':
    p1 = Producto(12, "ColaCola", 1, 1.55, 100)
    serializarPickle("../ficheros/producto.bin", p1)
    obj = deserializarPickle("../ficheros/producto.bin")
    print(obj)

    t1 = Time(12,30,45)
    d1 = Date(20,6,2024)
    serializarShelve("../ficheros/objetos", prod=p1, hora=t1, fecha=d1)
