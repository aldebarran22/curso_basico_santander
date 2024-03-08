"""
Implementar las operaciones CRUD para una entidad
de la base de datos
C - Create: insert into
R - Read: select ... where id=PK
U - Update: update
D - Delete: delete
select: select all
"""

import sqlite3 as db
from os.path import isfile


class Empleado:
    def __init__(self, id=0, nombre="", cargo=""):
        self.__id = id
        self.__nombre = nombre
        self.__cargo = cargo

    def getId(self):
        return self.__id

    def setId(self, id):
        self.__id = id

    def getNombre(self):
        return self.__nombre

    def setNombre(self, nombre):
        self.__nombre = nombre

    def getCargo(self):
        return self.__cargo

    def setCargo(self, cargo):
        self.__cargo = cargo

    def getTupla(self):
        return (self.__nombre, self.__cargo)

    def getTupla2(self):
        return (self.__nombre, self.__cargo, self.__id)

    def __str__(self):
        return str(self.__id) + " " + self.__nombre + " " + self.__cargo

    def __repr__(self):
        return str(self)
    
class EmpleadoBD:
    """Implementar las operaciones CRUD"""

    def __init__(self, path):
        
        if not isfile(path):
            raise FileNotFoundError(f"No existe la BD: {path}")
        
        self.con = db.connect(path)

    def __del__(self):
        self.con.close()

if __name__ == '__main__':
    try:
        empBD = EmpleadoBD('../bd/empresa3.db')
    except Exception as e:
        print(e)

     
