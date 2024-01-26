"""
Crear la conexión a la BD (comprobando si existe el fichero)
y lanzar consultas
"""
import sqlite3 as db
from os.path import isfile


def listarTabla(path, tabla):
    if isfile(path):
        con = db.connect(path)
        print('conexión ok')
    else:
        raise FileNotFoundError(f"El fichero {path} no existe...")
        


if __name__ == "__main__":
    path = "../bd/empresa3.db"
    listarTabla(path, "clientes")
