"""
Conexión a la BD sqlite3 con Python
"""
import sqlite3 as dbapi
from os.path import isfile


def test(path):
    conexion = None
    try:
        if isfile(path):
            conexion = dbapi.connect(path)
        else:
            raise FileNotFoundError(f"El fichero {path} no existe")
    except Exception as e:
        print(e)
    finally:
        if conexion:
            conexion.close()

if __name__ == '__main__':
    test("empresa.db")    