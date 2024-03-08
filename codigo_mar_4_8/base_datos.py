"""
Conectar con sqlite3 y ejecutar consultas
"""

import sqlite3 as dbapi
from os.path import isfile
import sys


def isfloat(cad):
    return cad.replace(".", "").isnumeric()


def tuplaToCSV(t):
    csv = ";".join([str(i).replace(".", ",") if isfloat(i) else str(i) for i in t])
    return csv


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
                linea = tuplaToCSV(t)
                print(linea, file=file)

    except Exception as e:
        print(e)
    finally:
        if cur:
            cur.close()
        if con:
            con.close()


def exportar(path, tabla):
    pathTabla = f"../ficheros/{tabla}.csv"
    fich = open(pathTabla, "w")
    imprimirTabla(path, tabla, fich)
    fich.close()


if __name__ == "__main__":
    # imprimirTabla("../bd/empresa3.db", "empleados")
    exportar("../bd/empresa3.db", "pedidos")
