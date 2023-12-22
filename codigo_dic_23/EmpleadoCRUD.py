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
