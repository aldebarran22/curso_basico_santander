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

    def read(self, pk):
        cur = None
        try:
            cur = self.con.cursor()
            sql = """select p.id as idp, p.nombre, c.id as idc, c.nombre as nombrecat, 
            p.precio, p.existencias from productos p inner join categorias c
            p.idcategoria = c.id where p.id = ?"""
            cur.execute(sql, (pk,))

            

    def __del__(self):
        if hasattr(self, 'con'):
            self.con.close()

if __name__=='__main__':
    try:
        bd = ProductoCRUD('../bd/empresa3.db')

    except Exception as e:
        print(e)
