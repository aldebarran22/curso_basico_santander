"""
Implementar las operaciones CRUD para una entidad
de la base de datos
C - Create: insert into
R - Read: select ... where id=PK
U - Update: update
D - Delete: delete
"""

import sqlite3 as db
from os.path import isfile


class BaseDatos:

    def __init__(self, path):
        if not isfile(path):
            raise FileNotFoundError(f"El fichero {path} no existe")

        self.con = db.connect(path)

    def __del__(self):
        self.con.close()


if __name__ == "__main__":
    bd = BaseDatos("../bd/empresa3.db")
