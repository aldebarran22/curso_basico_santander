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
from producto import Producto

class ProductoCRUD:

    def __init__(self, path):
        if not isfile(path):
            raise FileNotFoundError(f"No existe el fichero: {path}")
        else:
            self.con = db.connect(path)

    def select(self, categoria=None):
        cur = None
        try:
            cur = self.con.cursor()
            if not categoria:
                sql = "select * from productos"
                cur.execute(sql)

            else:
                sql = """select p.id, p.nombre, p.idcategoria, p.precio, 
                p.existencias from productos p inner join categorias c
                where c.nombre = ?"""
                cur.execute(sql, (categoria,))

            return [Producto(*t) for t in cur.fetchall()]

        except Exception as e:
            raise e
        finally:
            if cur: cur.close()


    def read(self, id):
        cur = None
        try:
            cur = self.con.cursor()
            sql = "select * from productos where id=?"
            cur.execute(sql, (id,))
            t = cur.fetchone()
            if t == None:
                raise ValueError(f"No existe el producto con clave: {id}")
            else:
                return Producto(*t)

        except Exception as e:
            raise e
        finally:
            if cur: cur.close()

    def __del__(self):
        if hasattr(self, "con"):
            self.con.close()

if __name__=="__main__":
    try:
        bd = ProductoCRUD("../../empresa3.db")
        prod = bd.read(1)
        print(prod)

        L = bd.select("Comidas")
        print(len(L), "productos")
        print(L[:3])
    except Exception as e:
        print(e.__class__.__name__, e)