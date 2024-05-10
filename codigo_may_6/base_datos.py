"""
Conectar con la BD sqlite3. Crear conexiones, cursores, exportar datos
"""

import sqlite3 as db
from os.path import isfile


def conexion(path):
    con = None
    try:
        if not isfile(path):
            raise FileNotFoundError(f"No existe el fichero: {path}")

        con = db.connect(path)
        print("conexion ok!")

    except Exception as e:
        print(e)

    finally:
        if con:
            con.close()


if __name__ == "__main__":
    conexion("../../bd/empresa3.db")
