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

if __name__=="__main__":
    try:
        bd = ProductoCRUD("../../empresa3.db")
        prod = bd.read(1)
        print(prod)

        prod.precio = 2.5
        prod.existencias = 50
        if bd.update(prod):
            print('Registro actualizado')
        else:
            print('No se ha podido actualizar')

        L = bd.select("Bebidas")
        print(len(L), "productos")
        print(L[:3])

        if bd.delete(88):
            print('producto borrado')
        else:
            print('no se ha podido eliminar')

        """
        nuevo = Producto(0, "ColaCola3", 1, 1.8, 230)
        if bd.create(nuevo):
            print('Registro creado: ', nuevo.id)
        else:
            print('no se ha creado')
        """

    except Exception as e:
        print(e.__class__.__name__, e)