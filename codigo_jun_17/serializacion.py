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

if __name__ == '__main__':
    p1 = Producto(12, "ColaCola", 1, 1.55, 100)
    serializarPickle("..ficheros/producto.bin", p1)

