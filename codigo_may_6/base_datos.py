"""
Conectar con la BD sqlite3. Crear conexiones, cursores, exportar datos
"""

import sqlite3 as db
from os.path import isfile


def conexion(path, tabla):
    con = None
    cur = None
    try:
        if not isfile(path):
            raise FileNotFoundError(f"No existe el fichero: {path}")

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
    conexion("../../bd/empresa3.db")
