"""
Base de datos sqlite3
"""

import sqlite3 as db
from os.path import isfile
import sys

def conexion(path):
    con = None
    try:
        if not isfile(path):
            raise FileNotFoundError(f"No se encuentra el fichero: {path}")
        else:
            con = db.connect(path)

    except Exception as e:
        print(e)
    finally:
        if con: con.close()


def printTabla(path, tabla, sep=';', file=sys.stdout):
    con = None
    cur = None
    try:
        if not isfile(path):
            raise FileNotFoundError(f"No se encuentra el fichero: {path}")
        else:
            con = db.connect(path)
            cur = con.cursor()
            sql = f"select * from {tabla}"

            cur.execute(sql)
            cabs = sep.join([t[0] for t in cur.description])
            print(cabs, file=file)

            for t in cur.fetchall():
                csv = sep.join([str(i) if type(i)!=float \
                    else str(i).replace('.',',') for i in t])
                print(csv, file=file)

    except Exception as e:
        print(e)
    finally:
        if cur: cur.close()
        if con: con.close()

def exportarTabla(path, tabla, sep=";"):
    path_fich = f"../ficheros/{tabla}.csv"
    with open(path_fich, "w") as fich:
        printTabla(path, tabla, sep, fich)
    


if __name__=='__main__':
    exportarTabla("../bd/empresa3.db","pedidos")