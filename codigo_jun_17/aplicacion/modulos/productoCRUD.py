"""
Operaciones CRUD del producto de la BD:
C: Create -> insert into
R: Read -> select (pk)
U: Update -> update (pk)
D: Delete -> delete (pk)
select: select * from productos
"""

import sqlite3 as db
from os.path import isfile

class ProductoCRUD:

    def __init__(self, path):
        if not isfile(path):
            raise FileNotFoundError(f"No existe el fichero: {path}")
        else:
            self.con = db.connect(path)

    def __del__(self):
        self.con.close()

if __name__=="__main__":
    bd = ProductoCRUD("../empresa3.db")
    #prod = bd.read(1)
    #print(prod)