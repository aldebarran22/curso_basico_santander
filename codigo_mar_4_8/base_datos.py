"""
Conectar con sqlite3 y ejecutar consultas
"""

import sqlite3 as dbapi
from os.path import isfile


def imprimirTabla(path, tabla):
    con = None
    cur = None
    try:
        if not isfile(path):
            raise FileNotFoundError(f"No se encontró el fichero: {path}")

        else:
            con = dbapi.connect(path)
            sql = f"select * from {tabla}"
            cur = con.cursor()
            cur.execute(sql)
            for t in cur.fetchall():
                print(t)

    except Exception as e:
        print(e)
    finally:
        if cur:
            cur.close()
        if con:
            con.close()


if __name__ == "__main__":
    imprimirTabla("../bd/empresa3.db", "pedidos")
