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


def listar(path, tabla):
    con = None
    cur = None
    try:
        if not isfile(path):
            raise FileNotFoundError(f"No se ha encontrado el fichero: {path}")
        else:
            con = db.connect(path)
            sql = f"select * from {tabla}"
            cur = con.cursor()
            cur.execute(sql)

            print(cur.description)



    except Exception as e:
        print(e.__class__.__name__, e)

    finally:
        if cur:
            cur.close()
        if con:
            con.close()


if __name__ == "__main__":
    testConexion("../../bd/empresa3.db")
