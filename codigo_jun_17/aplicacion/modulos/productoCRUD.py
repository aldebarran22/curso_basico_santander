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
from modulos.producto import Producto

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
                on p.idcategoria = c.id where c.nombre = ?"""
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

    def delete(self, id):
        sql = "delete from productos where id=?"
        t = (id, )
        return self.__delete_update(sql, t)

    def update(self, prod):
        sql = """update productos set nombre=?, idcategoria=?, 
        precio=?, existencias=? where id=?"""
        t = prod.getTupla() + (prod.id, )
        return self.__delete_update(sql, t)


    def __delete_update(self, sql, tupla):
        cur = None
        try:
            cur = self.con.cursor()
            cur.execute(sql ,tupla)
            n = cur.rowcount
            self.con.commit()
            return n==1

        except Exception as e:
            self.con.rollback()
            raise e

        finally:
            if cur: cur.close()

    def create(self, nuevo):
        cur = None
        try:
            cur = self.con.cursor()
            sql = """insert into productos(nombre, idcategoria, precio, existencias)
            values(?,?,?,?)"""
            cur.execute(sql, nuevo.getTupla())
            nuevo.id = cur.lastrowid
            n = cur.rowcount
            self.con.commit()
            return n==1

        except Exception as e:
            self.con.rollback()
            raise e

        finally:
            if cur: cur.close()

    def __del__(self):
        if hasattr(self, "con"):
            self.con.close()

