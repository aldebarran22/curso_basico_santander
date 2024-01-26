"""
Crear la conexión a la BD (comprobando si existe el fichero)
y lanzar consultas
"""
import sqlite3 as db
from os.path import isfile


def listarTabla(path, tabla):
    pass


if __name__ == "__main__":
    path = "noexiste.db"
    listarTabla(path, "clientes")
