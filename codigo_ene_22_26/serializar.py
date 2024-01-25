"""
Serializar objetos con pickle: para 1 sólo objeto y shelve: para varios
Se puede tratar como un diccionario
"""
import pickle as p
from fecha_hora import DateTime


def serializarPickle(path, objeto):
    fich = None
    try:
        # Abrir el fichero binario para escritura
        fich = open(path, "wb")
        p.dump(objeto, fich, 0)

    except Exception as e:
        print(e)
    finally:
        if fich:
            fich.close()
