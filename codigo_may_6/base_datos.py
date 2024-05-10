"""
Conectar con la BD sqlite3. Crear conexiones, cursores, exportar datos

CRUD:
Create -> insert into
Read -> select (pk)
Update -> update (pk)
delete -> delete (pk)
select
"""

import sqlite3 as db
import sys
from os.path import isfile


def conexion(path, tabla, file=sys.stdout, sep=";"):
    con = None
    cur = None
    try:
        if not isfile(path):
            raise FileNotFoundError(f"No existe el fichero: {path}")

        con = db.connect(path)
        cur = con.cursor()
        sql = f"select * from {tabla}"
        cur.execute(sql)
        cabs = sep.join([t[0] for t in cur.description])
        print(cabs, file=file)
        for t in cur.fetchall():
            fila = sep.join(
                [
                    str(i).replace(".", ",") if isinstance(i, float) else str(i)
                    for i in t
                ]
            )
            print(fila, file=file)

    except Exception as e:
        print(e)

    finally:
        if cur:
            cur.close()
        if con:
            con.close()


def exportar(path, tabla, sep=";"):
    path_file = f"../ficheros/{tabla}.csv"
    fich = open(path_file, "w")
    conexion(path, tabla, fich, sep)
    fich.close()


def testExportar():
    conexion("../../bd/empresa3.db", "pedidos")
    exportar("../../bd/empresa3.db", "pedidos")


class BaseDatos:

    def __init__(self, path):
        if not isfile(path):
            raise FileNotFoundError(f"No existe el fichero: {path}")
        self.con = db.connect(path)

    def __del__(self):
        if hasattr(self, "con"):
            self.con.close()


def testBaseDatos():
    try:
        bd = BaseDatos("../../bd/empresa33.db")
    except Exception as e:
        print(e)


if __name__ == "__main__":
    testBaseDatos()
