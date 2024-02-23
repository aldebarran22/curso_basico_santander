"""
Base de datos: SQLite3
"""

import sqlite3 as db
from os.path import isfile


def listar(path, tabla):
    con = None
    try:
        if not isfile(path):
            raise FileNotFoundError(f"No existe el fichero: {path}")
        else:
            con = db.connect(path)
            print("conexión Ok!")
    except Exception as e:
        print(e)
    finally:
        if con:
            con.close()
