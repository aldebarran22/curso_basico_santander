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

def printTabla(path, tabla):
    con = None
    try:
        if not isfile(path):
            raise FileNotFoundError(f"No existe el fichero: {path}")
        
        con = db.connect(path)
        cur = con.cursor()

        sql = f"select * from {tabla}"
        cur.execute(sql)

        print(cur.description)

    except Exception as e:
        raise e
    finally:
        if con: con.close()

if __name__ == '__main__':
    try:
        #conexion("../../empresa3.db")
        printTabla("../../empresa3.db", "pedidos")
    except Exception as e:
        print(e)