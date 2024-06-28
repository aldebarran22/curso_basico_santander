"""
Base de datos sqlite3 con Python
Conexiones, cursores, obtener resultados,
sql parametrizado
"""

import sqlite3 as db
from os.path import isfile
import sys


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


def listar(path, tabla, sep=";", file=sys.stdout):
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

            cabs = sep.join([t[0] for t in cur.description])
            print(cabs, file=file)

            for t in cur.fetchall():
                datos = sep.join([str(i) for i in t])
                print(datos, file=file)

    except Exception as e:
        print(e.__class__.__name__, e)

    finally:
        if cur:
            cur.close()
        if con:
            con.close()


if __name__ == "__main__":
    # testConexion("../../bd/empresa3.db")
    listar("../../bd/empresa3.db", "productos")
