"""
Conectar con sqlite3 y ejecutar consultas
"""

import sqlite3 as dbapi
from os.path import isfile


def imprimirTabla(path, tabla):
    con = None
    try:
        if not isfile(path):
            raise FileNotFoundError(f"No se encontró el fichero: {path}")

        else:
            print("conectado!")
            con = dbapi.connect(path)

    except Exception as e:
        print(e)
    finally:
        if con:
            con.close()


if __name__ == "__main__":
    imprimirTabla("../bd/empresa3.db", "pedidos")
