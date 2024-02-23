"""
Base de datos: SQLite3
"""

import sqlite3 as db
from os.path import isfile
import sys


def listar(path, tabla, file=sys.stdout):
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
            cabs = ";".join([t[0] for t in cur.description])
            print(cabs, file=file)
            for fila in cur.fetchall():
                cad = ";".join(str(i) for i in fila)
                print(cad, file=file)
    except Exception as e:
        print(e)
    finally:
        if cur:
            cur.close()
        if con:
            con.close()


def exportar(path, tabla):
    fich = open(f"../csv/{tabla}.csv", "w")
    listar(path, tabla, fich)
    fich.close()


if __name__ == "__main__":
    path = "../bd/empresa3.db"
    exportar(path, "empleados")
