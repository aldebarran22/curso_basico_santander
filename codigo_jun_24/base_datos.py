"""
Base de datos sqlite3 con Python
Conexiones, cursores, obtener resultados,
sql parametrizado
"""

import sqlite3 as db
from os.path import isfile


def testConexion(path):
    con = None
    try:
        if not isfile(path):
            raise FileNotFoundError(f"No se ha encontrado el fichero: {path}")
        else:
            con = db.connect(path)
            print("conexión ok!")

    except Exception as e:
        print(e.__class__.__name__, e)

    finally:
        if con:
            con.close()


if __name__ == "__main__":
    testConexion("no existe.dat")
