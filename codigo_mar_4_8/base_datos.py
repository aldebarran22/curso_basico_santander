"""
Conectar con sqlite3 y ejecutar consultas
"""

import sqlite3 as dbapi
from os.path import isfile
import sys


def imprimirTabla(path, tabla, file=sys.stdout):
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
            cabs = ";".join([t[0] for t in cur.description])
            print(cabs, file=file)
            for t in cur.fetchall():
                linea = ";".join([str(i) for i in t])
                print(linea, file=file)

    except Exception as e:
        print(e)
    finally:
        if cur:
            cur.close()
        if con:
            con.close()


if __name__ == "__main__":
    imprimirTabla("../bd/empresa3.db", "empleados")
