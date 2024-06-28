"""
Implementar las operaciones CRUD de una entidad de la base de datos:
C - Create -> insert into
R - Read -> select (pk)
U - Update -> update (pk)
D - Delete -> delete (pk)

select 
"""
import sqlite3 as db
from os.path import isfile

class ProductoCRUD:
    """Operaciones CRUD para un producto"""

    def __init__(self, path):
        if not isfile(path):
            raise FileNotFoundError(f"No se ha encontrado el fichero: {path}")
        else:
            self.con = db.connect(path)

    def __del__(self):
        self.con.close()

if __name__ == '__main__':
    try:
        bd = ProductoCRUD("../../bd/empresa3.db")

    except Exception as e:
        print(e)