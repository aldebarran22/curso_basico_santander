"""
Implementación de las operaciones CRUD:
Create -> insert into
Read -> select (pk)
Update -> update
Delete -> delete
select (categoria=None)
"""
import sqlite3 as db
from os.path import isfile

class Categoria:

    def __init__(self, id=0, nombre=""):
        self.id = id
        self.nombre = nombre

    def __str__(self):
        return str(self.id) + " " + self.nombre

    def __repr__(self):
        return str(self)


class Producto:

    def __init__(self, id=0, nombre="", cat=Categoria(), precio=0.0, exis=0):
        self.id = id
        self.nombre = nombre
        self.cat = cat
        self.precio = round(precio, 2)
        self.exis = exis

    def __str__(self):
        return (
            str(self.id)
            + " "
            + self.nombre
            + " "
            + str(self.cat)
            + " "
            + str(self.precio)
            + " "
            + str(self.exis)
        )

    def __repr__(self):
        return str(self)

    def getTupla(self):
        return (self.nombre, self.cat.id, self.precio, self.exis)

    def getTupla2(self):
        return (self.nombre, self.cat.id, self.precio, self.exis, self.id)

class ProductoCRUD:

    def __init__(self, path):

        if not isfile(path):
            raise FileNotFoundError(f"No se encuentra el fichero: {path}")
        else:
            self.con = db.connect(path)

    def __getProducto(self, t):
            cat = Categoria(*t[2:4])               
            t2 = t[:2]+(cat,)+t[4:]
            prod = Producto(*t2)
            return prod

    def read(self, pk):
        cur = None
        try:
            cur = self.con.cursor()
            sql = """select p.id as idp, p.nombre, c.id as idc, c.nombre as nombrecat, 
            p.precio, p.existencias from productos p inner join categorias c 
            on p.idcategoria = c.id where p.id = ?"""
            cur.execute(sql, (pk,))
            t = cur.fetchone()
            if t == None:
                raise ValueError(f"El producto con pk: {pk} no existe en la BD")
            else:
               return self.__getProducto(t)

        except Exception as e:
            raise e
        finally:
            if cur:cur.close()




    def __del__(self):
        if hasattr(self, 'con'):
            self.con.close()

if __name__=='__main__':
    try:
        bd = ProductoCRUD('../bd/empresa3.db')
        obj = bd.read(12)
        print(obj)

        L = bd.select()
        L = bd.select("Bebidas")

    except Exception as e:
        print(e)
