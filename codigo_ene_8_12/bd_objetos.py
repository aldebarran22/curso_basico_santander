import sqlite3 as dbapi
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
    def __init__(self, path):
        if not isfile(path):
            raise FileNotFoundError(f"No existe el fichero {path}")
        else:
            self.con = dbapi.connect(path)

    def __del__(self):
        if hasattr(self, "con"):
            self.con.close()


if __name__ == "__main__":
    try:
        bd = EmpleadoBD("../bd/empresa3.db")
        L = bd.select()
        print(f"Tenemos {len(L)} empleados")

        e1 = bd.read(1)
        print(e1)

        e1.setCargo("Gerente")
        if bd.update(e1) == 1:
            print("Registro actualizado")

        """
        nuevo = Empleado(0, "Sandra", "Gerente")
        if bd.create(nuevo) == 1:
            print("Registro creado")
            print(nuevo)
        """

        if bd.delete(150) == 1:
            print("Registro borrado")

    except Exception as e:
        print(e)
