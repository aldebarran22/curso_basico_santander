"""
Base de datos: SQLite3
"""

import sqlite3 as db
from os.path import isfile


def listar(path, tabla):
    con = None
    cur = None
    try:
        if not isfile(path):
            raise FileNotFoundError(f"No existe el fichero: {path}")
        else:
            con = db.connect(path)
            cur = con.cursor()
            sql = f"select * from {tabla}"
            cur.execute(sql)
            print(cur.description)
    except Exception as e:
        print(e)
    finally:
        if cur:
            cur.close()
        if con:
            con.close()


if __name__ == "__main__":
    path = "../bd/empresa3.db"
    listar(path, "pedidos")
