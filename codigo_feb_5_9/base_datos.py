import sqlite3 as db
from os.path import isfile

def conexion(path):
    if not isfile(path):
        raise FileNotFoundError(f"El fichero {path} no existe")
    else:
        pass


if __name__ == '__main__':
    conexion('../bd/empresa3.db')
