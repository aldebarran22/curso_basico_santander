"""
Conexión a la BD, ejecutar consultas
EmpleadoCRUD
C: Create --> insert into
R: Read --> select (pk)
U: Update 
D: Delete 
"""

import sqlite3 as db
from os.path import isfile
import sys

def conexion(path):
    con = None
    try:
        if not isfile(path):
            raise FileNotFoundError(f"No existe el fichero: {path}")
        
        con = db.connect(path)
        print('Conexión ok!')

    except Exception as e:
        raise e
    finally:
        if con: con.close()

def printTabla(path, tabla, file=sys.stdout, sep=";"):
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
            fila = sep.join([str(i) for i in t])
            print(fila, file=file)

    except Exception as e:
        raise e
    finally:
        if cur: cur.close()
        if con: con.close()

def exportarTabla(path, tabla, sep=";"):
    path_file = f"../ficheros/{tabla}.csv"
    fich = open(path_file, "w")
    printTabla(path, tabla, file=fich, sep=sep)
    fich.close()


if __name__ == '__main__':
    try:
        #conexion("../../empresa3.db")
        printTabla("../../empresa3.db", "categorias")
    except Exception as e:
        print(e)