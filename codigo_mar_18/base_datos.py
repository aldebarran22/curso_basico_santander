"""
Conectar con la bd, crear cursores, extraer registros
"""

import sqlite3 as db
from os.path import isfile


def listar(path):
    con = None
    try:
        if not isfile(path):
            raise FileNotFoundError(f"El fichero: {path} no existe")
        con = db.connect(path)
        print("conexión ok!")

    except Exception as e:
        print(e)
    finally:
        if con:
            con.close()


if __name__ == "__main__":
    listar("../bd/empresa3.db")
