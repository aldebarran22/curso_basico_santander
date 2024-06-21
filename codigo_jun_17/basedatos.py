"""
Conectar con la bd de sqlite3 y extraer registros (exportar a ficheros)
"""

import sqlite3 as db
from os.path import isfile

def listarTabla(path, tabla):
    con = None
    try:
        if not isfile(path):
            raise FileNotFoundError(f"No se encuentra el fichero: {path}")
        else:
            # Abrir la conexión con la BD:
            con = db.connect(path)
            print("conexión ok")

    except Exception as e:
        raise e
    finally:
        if con: con.close()

if __name__=='__main__':
    try:
        listarTabla("empresa3.db", "productos")
    except Exception as e:
        print(e)
