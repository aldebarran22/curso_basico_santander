"""
Conectar con la bd, crear cursores, 
extraer registros
"""

import sqlite3 as db
from os.path import isfile
import sys
from formatos import isfloat


def listar(path, tabla, file=sys.stdout):
    con = None
    cur = None
    try:
        if not isfile(path):
            raise FileNotFoundError(f"El fichero: {path} no existe")
        con = db.connect(path)
        # print("conexión ok!")
        cur = con.cursor()
        sql = f"select * from {tabla}"
        cur.execute(sql)
        cabs = ";".join([t[0] for t in cur.description])
        print(cabs, file=file)
        for t in cur.fetchall():
            L = [str(i) for i in t]
            L = [i.replace('.',',') if isfloat(i) else i for i in L]
            linea = ";".join(L)
            print(linea, file=file)

    except Exception as e:
        print(e)
    finally:
        if cur:
            cur.close()
        if con:
            con.close()


def exportar(path, tabla):
    path_fich = f"../ficheros/{tabla}.csv"
    fich = open(path_fich, "w")
    listar(path, tabla, fich)
    fich.close()


if __name__ == "__main__":
    # listar("../bd/empresa3.db", "productos")
    exportar("../bd/empresa3.db", "productos")
