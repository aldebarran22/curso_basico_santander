"""
Base de datos sqlite3
"""

import sqlite3 as db
from os.path import isfile

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

if __name__=='__main__':
    conexion("../bd/empresa33.db")