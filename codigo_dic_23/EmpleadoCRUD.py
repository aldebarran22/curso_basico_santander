"""
Implementar las operaciones CRUD (create - read - update - delete)
para los empleados de la base de datos.
"""
from os.path import isfile
import sqlite3 as dbapi


class Empleado:
    def __init__(self, id=0, nombre="", cargo=""):
        self.__id = id
        self.__nombre = nombre
        self.__cargo = cargo

    def getTupla(self):
        return (self.__id, self.__nombre, self.__cargo)

    def __str__(self):
        return str(self.__id) + " " + self.__nombre + " " + self.__cargo

    def __repr__(self):
        return str(self)


class EmpleadoBD:
    def __init__(self, path):
        if not isfile(path):
            raise FileNotFoundError(f"El fichero {path} no existe")
        else:
            self.con = dbapi.connect(path)

    def __del__(self):
        if hasattr(self, "con"):
            self.con.close()


if __name__ == "__main__":
    try:
        bd = EmpleadoBD("../bd/empresa3.db")
    except Exception as e:
        print(e)
