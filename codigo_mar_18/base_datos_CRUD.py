"""Operaciones CRUD para un producto
C - Create -> insert into
R - Read -> select por PK
U - Update -> update
D - Delete -> delete
"""

from os.path import isfile
import sqlite3 as dbapi


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
        return (self.id, self.nombre, self.cat.id, self.precio, self.exis)

    def getTupla2(self):
        return (self.nombre, self.cat.id, self.precio, self.exis, self.id)


class BaseDatos:

    def __init__(self, path):
        if not isfile(path):
            raise FileNotFoundError(f"El fichero: {path} no existe")

        self.con = dbapi.connect(path)

    def __del__(self):
        if hasattr(self, "con"):            
            self.con.close()
            print("Conexión  cerrada!")


if __name__ == "__main__":
    try:
        bd = BaseDatos("../bd/empresa3.db")
        #prod = bd.read(3)
        #print(prod)
    except Exception as e:
        print(e)
