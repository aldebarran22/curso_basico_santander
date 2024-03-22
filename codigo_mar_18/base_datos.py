"""
Conectar con la bd, crear cursores, 
extraer registros
"""

import sqlite3 as db
from os.path import isfile


def listar(path, tabla):
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
        print(cabs)
        for t in cur.fetchall():
            linea = ";".join([str(i) for i in t])
            print(linea)

    except Exception as e:
        print(e)
    finally:
        if cur:
            cur.close()
        if con:
            con.close()


if __name__ == "__main__":
    listar("../bd/empresa3.db", "productos")
