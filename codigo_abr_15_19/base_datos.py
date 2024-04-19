"""
Conectar con la BD de SQLite3. Crear conexiones, cursores, ejecutar
consultas ...
"""

import sqlite3 as db
from os.path import isfile
import sys

def conexion(path):
    con = None
    try:
        if not isfile(path):
            raise FileNotFoundError(f"No se encuentra el fichero: {path}")

        con = db.connect(path)
        print("Conexión ok!")

    except Exception as e:
        print(e)
    finally:
        if con:
            con.close()

def imprimirTabla(path, tabla, file=sys.stdout):
    con = None
    cur = None
    try:
        if not isfile(path):
            raise FileNotFoundError(f"No se encuentra el fichero: {path}")

        con = db.connect(path)
        cur = con.cursor()
        sql = f"select * from {tabla}"

        cur.execute(sql)
        print(cur.description)


    except Exception as e:
        print(e)
    finally:
        if con:
            con.close()


if __name__ == "__main__":
    conexion("../bd/empresa3.db")
