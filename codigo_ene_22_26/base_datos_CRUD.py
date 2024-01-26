"""
OPERACIONES CRUD:
C: create --> insert into
R: Read --> select pk
U: Update --> update
D: delete --> delete
select: recuperar una colección
"""

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

    def read(self, id):
        sql = "select id,nombre,cargo from empleados where id=?"
        cur = self.con.cursor()
        cur.execute(sql, (id,))
        t = cur.fetchone()
        if t == None:
            raise ValueError(f"El empleado con id: {id} no existe en la BD")
        else:
            return Empleado(*t)

    def create(self, emp):
        cur = None
        try:
            cur = self.con.cursor()
            sql = "insert into empleados(nombre, cargo) values(?,?)"
            cur.execute(sql, emp.getTupla())
            emp.setId(cur.lastrowid)
            self.con.commit()

        except Exception as e:
            self.con.rollback()
            raise e
        finally:
            if cur:
                cur.close()

    def select(self, cargo=None):
        sql = "select id,nombre,cargo from empleados"
        cur = self.con.cursor()
        if cargo:
            sql += " where cargo = ?"
            cur.execute(sql, (cargo,))
        else:
            cur.execute(sql)
        return [Empleado(*t) for t in cur.fetchall()]

    def __del__(self):
        if hasattr(self, "con"):
            self.con.close()


if __name__ == "__main__":
    try:
        bd = EmpleadoBD("../bd/empresa3.db")
        L = bd.select("Gerente")
        print("Tenemos: ", len(L), "empleados")

        emp = bd.read(4)
        print(emp)

        emp2 = Empleado(0, "Jorge Sanz", "Ventas")
        bd.create(emp2)
        print(emp2)

    except Exception as e:
        print(e)
