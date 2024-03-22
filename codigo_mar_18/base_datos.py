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
        #print("conexión ok!")
        cur = con.cursor()
        sql = f"select * from {tabla}"
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
    listar("../bd/empresa3.db", "empleados")
